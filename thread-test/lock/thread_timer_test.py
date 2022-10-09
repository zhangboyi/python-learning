#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/23 22:44
# @Author:boyizhang
import threading
from threading import Timer


class Example_1():

    def run(self):
        print('hello world.')

    def main_run(self,sleep_time=3):
        print(f'pre run.')
        t = Timer(sleep_time,self.run)
        t.start()
        print(f'name: {t.name} done.')
        return t

if __name__ == '__main__':
    e1 = Example_1()
    t = e1.main_run()
    # t.cancel()
    print(f'main_thread: {threading.currentThread().name}')
