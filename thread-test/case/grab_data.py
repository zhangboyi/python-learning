#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/31 00:13
# @Author:boyizhang
import concurrent
import json
import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import Dict
from urllib.parse import urljoin
import traceback

import pandas as pd
import requests
from lxml import etree
from loguru import logger as log


class Tools():
    @staticmethod
    def load_time(func):
        def wrapper(*args, **kwargs):

            log.info(f'calling func: {func}')

            ctime = time.time() * 1000
            res = func(*args, **kwargs)
            mtime = time.time() * 1000
            log.info(f'call func: {func}.actual excution time is {mtime - ctime} ms')
            return res

        return wrapper

    @staticmethod
    def print_log(func, ):
        pass


class CrawlDataFromBK():
    def __init__(self, executor_num=5, max_retry_count=10, max_retry_time_sleep=2, debug=False,debug_city_num=1,debug_area_url_num=1):
        self.city_area_data_total_num_dict = dict()
        self.separator = '::'
        self.request_url_error = list()
        self.generate_area_url_by_city_error = defaultdict(list)
        self.generate_area_data_url_error = defaultdict(list)
        # 线程数量
        self.executor_num = executor_num
        self.max_retry_count = max_retry_count
        self.max_retry_time_sleep = max_retry_time_sleep
        # generate_city_url 加debug限制
        # generate_area_url_by_city
        self.debug = debug
        self.debug_city_num = debug_city_num
        self.debug_area_url_num = debug_area_url_num

    @Tools.load_time
    def generate_city_url(self):
        """
        获取各个城市小区房的url
        :return:
        """
        url = "https://www.ke.com/city/"

        resp = self.custom_request('GET', url)
        if resp.status_code != 200:
            sys.exit(-1)

        hm = etree.HTML(resp.text)
        pp = hm.xpath(
            '/html/body/div[3]/div[2]/div[1]/div[2]/ul/li[*]/div[2]/div/ul/li[*]/a')

        city_url_dict = {}
        for i, item in enumerate(pp):
            # todo debug
            if self.debug and i > self.debug_city_num:
                log.info("debug skip")
                break
            city_name = item.xpath("./text()")[0]
            city_url = "https:" + item.xpath("./@href")[0] + "/xiaoqu/"
            city_url_dict[city_name] = city_url
        log.info(f'generate_city_url success. city_url_dict:{city_url_dict}')

        return city_url_dict

    @Tools.load_time
    def generate_area_url_by_city(self, city_url_dict: Dict):
        """
        访问各个城市的url，获取各个城市的各个区域的url
        :param city_url_dict:
        :return:
        {
            "深圳:南山区":[]
        }
        """
        city_area_url_dict = defaultdict(list)
        i = 1
        for city_name, city_url in city_url_dict.items():

            log.info(f'total: {len(city_url_dict)}, Processing: {i}')
            i += 1
            # 提取行政区名称和地址
            resp = self.custom_request('GET', city_url)
            if resp.status_code != 200:
                self.generate_area_url_by_city_error[city_name].append(city_url)
                continue
            hm = etree.HTML(resp.text)
            log.info(hm)
            # city_name = hm.xpath('//*[@class="resultDes clear"]//a/text()')[0][0:2]
            # 提取行政区名称和地址
            city_areas = hm.xpath('//*[@id="beike"]/div[1]/div[3]/div[1]/dl[2]/dd/div/div/a')
            for i,city_area in enumerate(city_areas):
                # todo debug
                if self.debug and i > self.debug_area_url_num:
                    log.info("debug skip")
                    break
                area_name = city_area.xpath("./text()")[0]  # 行政区名称
                area_url = urljoin(
                    city_url, city_area.xpath("./@href")[0])  # 行政区地址
                key = f'{city_name}::{area_name}'
                city_area_url_dict[city_name].append(area_url)

        log.info(
            f'generate_area_url_by_city success. city_area_url_dict:{city_area_url_dict}')
        return city_area_url_dict

    @Tools.load_time
    def generate_area_url_by_city_mutil_thread(self, city_url_dict: Dict):
        city_area_url_dict = defaultdict(list)
        with ThreadPoolExecutor(self.executor_num) as executor:
            future_dict = {executor.submit(self.custom_request, 'GET', city_url) : city_name for city_name, city_url in
                           city_url_dict.items()}
            # 等同上一条语句
            # future_dict = dict()
            # for city_name, city_url in city_url_dict.items():
            #     future_dict[executor.submit(self.custom_request,city_url)]=city_name
            for future in concurrent.futures.as_completed(future_dict):
                city_name = future_dict[future]
                city_url = city_url_dict[city_name]
                try:
                    resp = future.result()
                    hm = etree.HTML(resp.text)
                    if resp.status_code != 200:
                        self.generate_area_url_by_city_error[city_name].append(city_url)
                        raise Exception(f'request url:{city_url} is error')
                    # city_name = hm.xpath('//*[@class="resultDes clear"]//a/text()')[0][0:2]
                    # 提取行政区名称和地址
                    city_areas = hm.xpath('//*[@id="beike"]/div[1]/div[3]/div[1]/dl[2]/dd/div/div/a')
                    for i,city_area in enumerate(city_areas):
                        # todo debug
                        if self.debug and i > self.debug_area_url_num:
                            log.info("debug skip")
                            break
                        area_name = city_area.xpath("./text()")[0]  # 行政区名称
                        area_url = urljoin(
                            city_url, city_area.xpath("./@href")[0])  # 行政区地址
                        # key = f'{city_name}::{area_name}'
                        city_area_url_dict[city_name].append(area_url)
                except Exception as e:
                    log.info('%r generated an exception: %s' % (city_name, e))
        log.info(
            f'generate_area_url_by_city success. city_area_url_dict:{city_area_url_dict}')
        return city_area_url_dict

    @Tools.load_time
    def generate_area_data_url(self, city_area_url_dict):
        city_area_data_url_dict = defaultdict(list)
        city_area_data_total_num_dict = dict()
        for city_name, area_url_list in city_area_url_dict.items():
            for area_url in area_url_list:
                resp = self.custom_request('GET', area_url)
                if resp.status_code != 200:
                    self.generate_area_data_url_error[city_name].append(
                        area_url)
                    continue
                hm = etree.HTML(resp.text)
                total = hm.xpath('//*[@class="resultDes clear"]//span/text()')[0]
                city_area_data_total_num_dict[city_name] = int(total)
                totalPage = json.loads(hm.xpath('//*[@class="page-box house-lst-page-box"]/@page-data')[0])[
                    "totalPage"]
                for i in range(1, totalPage + 1):
                    area_data_url = f"{area_url}"
                    if i != 1:
                        area_data_url += f'pg{i}/'
                    city_area_data_url_dict[city_name].append(
                        area_data_url)
        log.info(
            f'generate_area_data_url success. city_area_data_url_dict:{city_area_data_url_dict}.\n city_area_data_total_num_dict:{city_area_data_total_num_dict}.')
        return city_area_data_url_dict, city_area_data_total_num_dict

    @Tools.load_time
    def generate_area_data_url_by_mutil_thread(self, city_area_url_dict):
        city_area_data_url_dict = defaultdict(list)
        city_area_data_total_num_dict = dict()
        for city_name, area_url_list in city_area_url_dict.items():
            with ThreadPoolExecutor(self.executor_num) as executor:
                future_dict = {executor.submit(self.custom_request, 'GET', area_url):area_url for area_url in area_url_list}

                for future in concurrent.futures.as_completed(future_dict):
                    area_url = future_dict[future]
                    try:
                        ctime = time.time()
                        resp = future.result()
                        if resp.status_code != 200:
                            self.generate_area_data_url_error[city_name].append(area_url)
                            continue
                        hm = etree.HTML(resp.text)
                        total = hm.xpath('//*[@class="resultDes clear"]//span/text()')[0]
                        log.info(f"city_area_name:{city_name} - pre:{int(total)},{type(int(total))}")
                        # total = hm.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[2]/h2/span')
                        # log.info(f"af:{total}")
                        city_area_data_total_num_dict[city_name] = int(total)
                        if int(total) == 0:
                            continue
                        totalPage = json.loads(hm.xpath('//*[@class="page-box house-lst-page-box"]/@page-data')[0])[
                            "totalPage"]
                        if totalPage == 0:
                            continue
                        for i in range(1, totalPage + 1):
                            area_data_url = f"{area_url}"
                            if i != 1:
                                area_data_url += f'pg{i}/'
                            city_area_data_url_dict[city_name].append(
                                area_data_url)
                        mtime = time.time()
                        log.warning(f'AAAAA-{city_name}-{mtime-ctime}s')
                    except Exception as e:
                        log.info(f"e:{e}-{traceback.print_exc()}")
        log.info(
            f'generate_area_data_url success. city_area_data_url_dict:{city_area_data_url_dict}.\n city_area_data_total_num_dict:{city_area_data_total_num_dict}.')
        return city_area_data_url_dict, city_area_data_total_num_dict

    @Tools.load_time
    def crawl_data(self, url):

        resp = self.custom_request('GET', url).text
        hm = etree.HTML(resp)

        titles = hm.xpath(
            '//ul[@class="listContent"]/li[*]/div[1]/div[@class="title"]/a/text()')
        title_inters = hm.xpath(
            '//ul[@class="listContent"]/li[*]/div[1]/div[@class="title"]/a/@href')
        areas = hm.xpath(
            '//ul[@class="listContent"]/li[*]/div[1]/div[@class ="positionInfo"]/a[1]/text()')
        prices = hm.xpath(
            '//ul[@class="listContent"]/li[*]//div[@class="xiaoquListItemPrice"]//span/text()')

        # crawl_data_dict_list["标题"].extend(titles)
        # crawl_data_dict_list["链接"].extend(title_inters)
        # crawl_data_dict_list["行政区"].extend(areas)
        # crawl_data_dict_list["参考均价"].extend(prices)
        crawl_data_dict = dict()
        crawl_data_dict["标题"] = titles
        crawl_data_dict["链接"] = title_inters
        crawl_data_dict["行政区"] = areas
        crawl_data_dict["参考均价"] = prices
        return crawl_data_dict

    @Tools.load_time
    def main_crawl_data(self, city_area_data_url_dict,
                        city_area_data_total_num_dict):
        for city_name, area_data_urls in city_area_data_url_dict.items():
            crawl_data_dict_list = defaultdict(list)
            for data_url in area_data_urls:
                crawl_data_dict = self.crawl_data(data_url)
                crawl_data_dict_list["标题"].extend(crawl_data_dict.get('标题', None))
                crawl_data_dict_list["链接"].extend(crawl_data_dict.get('链接', None))
                crawl_data_dict_list["行政区"].extend(crawl_data_dict.get('行政区', None))
                crawl_data_dict_list["参考均价"].extend(crawl_data_dict.get('参考均价', None))
            self.write_to_excel(
                crawl_data_dict_list,
                city_name,
                city_area_data_total_num_dict)

    @Tools.load_time
    def main_crawl_data_by_mutil_thread(self, city_area_data_url_dict,
                                        city_area_data_total_num_dict):
        """
        每个地区的area多线程爬取
        :return:
        """
        city_data_urls = defaultdict(list)
        for city_name, area_data_urls in city_area_data_url_dict.items():
            # city_name = city_area_name.split('::')[0]
            city_data_urls[city_name].extend(area_data_urls)

        for city_name, area_data_urls in city_data_urls.items():
            crawl_data_dict_list = defaultdict(list)
            future_dict = dict()
            with ThreadPoolExecutor(self.executor_num) as executor:
                for data_url in area_data_urls:
                    future_dict[executor.submit(self.crawl_data, data_url)] = city_name

                for future in concurrent.futures.as_completed(future_dict):
                    city_name = future_dict[future]
                    try:
                        crawl_data_dict = future.result()
                        crawl_data_dict_list["标题"].extend(crawl_data_dict.get('标题', None))
                        crawl_data_dict_list["链接"].extend(crawl_data_dict.get('链接', None))
                        crawl_data_dict_list["行政区"].extend(crawl_data_dict.get('行政区', None))
                        crawl_data_dict_list["参考均价"].extend(crawl_data_dict.get('参考均价', None))
                    except Exception as e:
                        log.info(e)


            self.write_to_excel(
                crawl_data_dict_list,
                city_name,
                city_area_data_total_num_dict)

    @Tools.load_time
    def write_to_excel(self, crawl_data_dict_list, city_name, city_area_data_total_num_dict):
        total=0
        for item_city_name, num in city_area_data_total_num_dict.items():
            if city_name == item_city_name:
                total+=num

        crawl_num=0
        for crawl_data_list in crawl_data_dict_list.values():
            crawl_num+=len(crawl_data_list)
            break

        # 准备信息，写入文档
        log.info(f'data:{crawl_data_dict_list}')
        data0 = pd.DataFrame(crawl_data_dict_list)
        data0.to_excel(
            f"贝壳爬取{city_name}{crawl_num}个(总{total}个).xlsx",
            index=False)
        log.info(city_name, "写入成功")

    @Tools.load_time
    def custom_request(self, method, url, headers=None,
                       params=None, payload=None):
        if not headers:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            }
        log.info(f"request url:{url}")
        resp = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            data=payload)
        max_retry_count = self.max_retry_count
        max_retry_time_sleep = self.max_retry_time_sleep
        request_count = 1
        # log.info(resp.text)
        while (resp.status_code != 200 or resp.status_code == 200 and '您无法访问此网站' in resp.text ) and request_count < max_retry_count:

            if resp.text == 'list index out of range' or resp.status_code == 200:
                is_verify=False
                log.error(f'error resp:{resp.text[:1000]}')
                while not is_verify:
                    log.error(f'Please lift the restrictions manually. input 1(yes) or 0(break). url:{url}\n')
                    input_num = input(f'input num(0/1):')
                    log.info(f'verifying: {type(input_num)}-input_num:{input_num}')
                    if '1' == input_num or 1 == int(input_num):
                        is_verify=True
                    else:
                        return resp
                    # time.sleep(10)
            sleep_time = random.random() * max_retry_time_sleep
            log.info(
                f'[{request_count}]-sleep time:{sleep_time}s. retry request url :{url}')
            time.sleep(sleep_time)
            resp = requests.request(
                method,
                url,
                headers=headers,
                params=params,
                data=payload)
            request_count += 1


        if resp.status_code != 200:
            log.info(f"retry {max_retry_count} to request url:{url} is error. ")
            self.request_url_error.append(url)
        # else:
        #     log.info(f"retry {max_retry_count} to request url:{url} is error. ")
        #     pass
        return resp

    @Tools.load_time
    def print_erorr(self):
        log.info(f"self.generate_area_data_url_error:{self.generate_area_data_url_error}")
        log.info(f"self.generate_area_url_by_city_error:{self.generate_area_url_by_city_error}")

    @Tools.load_time
    def main_run_by_mutil_thread(self):
        city_url_dict = self.generate_city_url()
        city_area_url_dict = self.generate_area_url_by_city_mutil_thread(city_url_dict)
        city_area_data_url_dict, city_area_data_total_num_dict = self.generate_area_data_url_by_mutil_thread(
            city_area_url_dict)
        self.main_crawl_data_by_mutil_thread(city_area_data_url_dict, city_area_data_total_num_dict)

        # self.print_erorr()

    @Tools.load_time
    def main_run_by_single_thread(self):
        city_url_dict = self.generate_city_url()
        city_area_url_dict = self.generate_area_url_by_city(city_url_dict)
        city_area_data_url_dict, city_area_data_total_num_dict = self.generate_area_data_url(city_area_url_dict)
        self.main_crawl_data(city_area_data_url_dict, city_area_data_total_num_dict)

        self.print_erorr()


if __name__ == '__main__':
    cd = CrawlDataFromBK(debug=True,debug_city_num=1,debug_area_url_num=10,executor_num=10)
    # 单线程实现
    cd.main_run_by_single_thread()
    # 多线程实现
    # cd.main_run_by_mutil_thread()
