#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/10/11 19:58
# @Author:boyizhang
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/27 5:15 下午
# @Author:boyizhang
import json
import random

import requests
from locust import TaskSet, task, HttpUser, run_single_user
from locust.clients import ResponseContextManager
from locust.runners import logger


def common_request(resources=1535, collections=52):
    url = f"http://seller.shopee.sg/api/tsp/nonlive/init?language=en&resources={resources}&collections={collections}"

    payload = {}
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers, data=payload)

    jres = json.loads(response)
    resource_ids = list()
    collection_ids = list()
    if response.status_code == 200:
        hashes = jres.get('hashes', None)

        if hashes:
            resource_dict: dict = hashes.get('resource', None)
            collection_dict: dict = hashes.get('collection', None)
            if resource_dict:
                resource_ids = resource_dict.keys()
            if collection_dict:
                collection_ids = collection_dict.keys()

    return resource_ids, collection_ids


class ScUserTask(TaskSet):

    @task
    def get_tsp_init(self):
        resources = random.choice(self.user.resource_ids)
        collections = random.choice(self.user.collection_ids)
        path = f"/api/tsp/nonlive/init?language=en&resources={resources}&collections={collections}"

        with self.client.get(path, catch_response=True) as res:
            # 如果想同一接口不同参数放在同一组，可用下面这种方式
            # with self.client.get(path,catch_response=True,name="/s?wd=[wd]") as res:
            res: ResponseContextManager
            # 如果不满足，则标记为failure
            if res.status_code != 200:
                res.failure(res.text)

    def on_start(self):
        logger.info('start....')

    def on_stop(self):
        logger.info('goodbye')


class SCUser(HttpUser):
    host = 'https://seller.shopee.sg'

    tasks = [ScUserTask, ]
    resource_ids, collection_ids = common_request()


if __name__ == '__main__':
    # run_single_user(SCUser)
    print(common_request())
