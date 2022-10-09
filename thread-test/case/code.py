#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/31 13:07
# @Author:boyizhang
import requests
import pandas as pd
from lxml import etree
from urllib.parse import urljoin
import json
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
dic = {}
url = "https://www.ke.com/city/"
resp = requests.get(url,headers = headers).text
hm =  etree.HTML(resp)
pp = hm.xpath('/html/body/div[3]/div[2]/div[1]/div[2]/ul/li[*]/div[2]/div/ul/li[*]/a')
city_inter = []
city_name0 = []
for item in pp:
    city_inter.append("https:"+item.xpath("./@href")[0]+"/xiaoqu/")
    city_name0.append(item.xpath("./text()")[0])
dic_ru = {}
#对全国城市进行循环
for i in range(len(city_inter)):
    #对无小区均价城市进行过滤
    if i>0:
        break
    try:
        url = city_inter[i]
        resp = requests.get(url, headers=headers).text
        hm = etree.HTML(resp)
        city_name = hm.xpath('//*[@class="resultDes clear"]//a/text()')[0][0:2]
        num_all = hm.xpath('//*[@class="resultDes clear"]//span/text()')[0]
        # 提取行政区名称和地址
        area = hm.xpath('//*[@id="beike"]/div[1]/div[3]/div[1]/dl[2]/dd/div/div/a')
        # 确定变量
        title = []
        title_inter = []
        area_n = []
        price = []
        # 对行政区案例进行循环
        for i,area_all in enumerate(area):
            if i>5:
                break
            # 对无案例行政区过滤
            try:
                area_name = area_all.xpath("./text()")[0]  # 行政区名称
                area_inter = urljoin(url, area_all.xpath("./@href")[0])  # 行政区地址
                resp1 = requests.get(area_inter, headers=headers).text
                hm1 = etree.HTML(resp1)
                page_all = json.loads(hm1.xpath('//*[@class="page-box house-lst-page-box"]/@page-data')[0])["totalPage"]
                # 将第一页的数据载入列表
                list1 = hm1.xpath('//ul[@class="listContent"]/li[*]/div[1]/div[@class="title"]/a/text()')
                for item1 in list1:
                    title.append(item1)
                list2 = hm1.xpath('//ul[@class="listContent"]/li[*]/div[1]/div[@class="title"]/a/@href')
                for item2 in list2:
                    title_inter.append(item2)
                list3 = hm1.xpath('//ul[@class="listContent"]/li[*]/div[1]/div[@class ="positionInfo"]/a[1]/text()')
                for item3 in list3:
                    area_n.append(item3)
                list4 = hm1.xpath('//ul[@class="listContent"]/li[*]//div[@class="xiaoquListItemPrice"]//span/text()')
                for item4 in list4:
                    price.append(item4)
                # 对2-尾页继续载入列表
                for i in range(2, (page_all + 1)):
                    url0 = f"{area_inter}pg{i}/"
                    resp2 = requests.get(url0, headers=headers).text
                    hm2 = etree.HTML(resp2)
                    list1 = hm2.xpath('//ul[@class="listContent"]/li[*]/div[1]/div[@class="title"]/a/text()')
                    for item1 in list1:
                        title.append(item1)
                    list2 = hm2.xpath('//ul[@class="listContent"]/li[*]/div[1]/div[@class="title"]/a/@href')
                    for item2 in list2:
                        title_inter.append(item2)
                    list3 = hm2.xpath('//ul[@class="listContent"]/li[*]/div[1]/div[@class ="positionInfo"]/a[1]/text()')
                    for item3 in list3:
                        area_n.append(item3)
                    list4 = hm2.xpath('//ul[@class="listContent"]/li[*]//div[@class="xiaoquListItemPrice"]//span/text()')
                    for item4 in list4:
                        price.append(item4)
                print("成功爬取：", city_name + area_name)
            except Exception as k:
                print(k)
                print(area_name,"无房源信息")
        num = len(title)  # 计算爬取数量
        print(city_name, "爬取完成，数量：", num,"总数：",num_all)
        # 准备信息，写入文档
        data = {}
        data["标题"] = title
        data["链接"] = title_inter
        data["行政区"] = area_n
        data["参考均价"] = price
        data0 = pd.DataFrame(data)
        data0.to_excel(f"贝壳爬取{city_name}{num}个(总{num_all}个).xlsx", index=False)
        print(city_name, "写入成功")
        dic_ru[city_name0[i]] = "写入成功"
    except Exception as e:
        dic_ru[city_name0[i]] = e
        print(city_name0[i],"无小区均价")
dict_ruture = {}
ru_city = list(dic_ru.keys())
ru_sta = list(dic_ru.values())
dict_ruture["城市"] = ru_city
dict_ruture["爬取结果"] = ru_sta
data_ru = pd.DataFrame(dict_ruture)
data_ru.to_excel("结果.xlsx")