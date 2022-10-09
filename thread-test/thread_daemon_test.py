#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/23 18:37
# @Author:boyizhang
import threading
import time

import requests


class Example_1():

    def __init__(self, *args, **kwargs):
        pass

    def run(self, sleep_time=1):
        current_thread = threading.current_thread()
        print(f'{threading.get_ident()}-waiting.')
        time.sleep(sleep_time)
        print(f'{threading.get_ident()}-runing.current_thread: {current_thread.name}')

    def request_http(self, sleep_time=1):
        current_thread = threading.current_thread()

        url = 'http://0.0.0.0:9999/'
        time.sleep(sleep_time)
        res = requests.get(url)

        print(f"res: {res},current_thread: {current_thread.name}")
        time.sleep(sleep_time)
        # 守护线程创建的子线程也是守护线程
        t1 = threading.Thread(target=self.run, name='thread-3')
        t1.start()
        print(f't1.Daemon: {t1.isDaemon()}')

    def main_run(self):
        t1 = threading.Thread(target=self.run)
        # t1.setDaemon(True)
        t1.start()
        # t1.join()
        print(f'main_thread-{threading.get_ident()}-runing.({threading.main_thread()})')

    def main_run_deamon(self):
        """
        标记为守护线程后，主线程销毁停止，守护线程一起销毁。

        :return:
        """
        t1 = threading.Thread(target=self.request_http, kwargs={"sleep_time": 1}, name='thread-1')
        t2 = threading.Thread(target=self.run, kwargs={"sleep_time": 4}, name='thread-2')
        # 设置为守护线程
        t1.setDaemon(True)
        t1.start()
        t2.start()

        print(f'main_thread-{threading.get_ident()}-runing.({threading.main_thread()})')


if __name__ == '__main__':
    e1 = Example_1()
    # e1.main_run()
    e1.main_run_deamon()
    # e1.request_http()
