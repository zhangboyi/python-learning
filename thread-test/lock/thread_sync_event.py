#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/21 21:04
# @Author:boyizhang
import os
import queue
import threading
import time
import random
from concurrent.futures import ProcessPoolExecutor

class Example_1():

    def __init__(self, *args, **kwargs):
        self.boys = ['此时一位捡瓶子的靓仔路过\n------------','此时一位没钱的网友路过\n------------','此时一位推着屎球的屎壳郎路过\n------------']
        self.event = threading.Event()
    def lighter(self):
        self.event.set()
        while 1:
            ti = (random.randint(1, 10))
            time.sleep(ti)
            print('等待 {} 秒后'.format(str(ti)))
            self.event.clear()
            time.sleep(ti)
            self.event.set()


    def go(self,boy):
        while 1:
            if self.event.is_set():
                # 如果事件被设置
                print('在辽阔的街头')
                print(boy)
                time.sleep(random.randint(1, 5))
            else:
                print('在寂静的田野')
                print(boy)
                self.event.wait()
                print('突然，一辆火车驶过')
                time.sleep(5)
    def main_run(self):

        t1 = threading.Thread(target=self.lighter)
        t1.start()

        for boy in self.boys:
            t2 = threading.Thread(target=self.go,args=(boy,))
            t2.start()

class Example_2():
    """
    消息订阅

    """

    def __init__(self, *args, **kwargs):
        self.envet = threading.Event()
        self.queue = queue.Queue()

    def consumer(self):
        while True:
            if self.envet.is_set():
                print(f'consumer-{threading.get_ident()}: {self.queue.get()}, size:{self.queue.qsize()}')
            else:
                print(f'no data to be consume,size:{self.queue.qsize()}')
                self.envet.wait()
            time.sleep(0.5)

    def product(self):
        while True:
            i=random.randint(1,1000000)
            self.queue.put(i)
            print(f'product: {i},size: {self.queue.qsize()}')
            if self.queue.qsize() >= 6:
                self.envet.set()
            else:
                self.envet.clear()
            time.sleep(0.5)

    def main_run(self):
        consumer_1 = threading.Thread(target=self.consumer)
        consumer_2 = threading.Thread(target=self.consumer)
        consumer_3 = threading.Thread(target=self.consumer)
        product_1 = threading.Thread(target=self.product)
        consumer_1.start()
        # consumer_2.start()
        consumer_3.start()
        product_1.start()
        # consumer_2.run()









if __name__ == '__main__':
    # e1 = Example_1()
    # e1.main_run()
    e2 = Example_2()
    e2.main_run()