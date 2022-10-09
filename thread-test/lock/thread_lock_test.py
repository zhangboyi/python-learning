#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/23 23:09
# @Author:boyizhang
import random
import threading
import time


class Example_1():

    def __init__(self, *args, **kwargs):
        self.lock = threading.Lock()
        self.custom_queue = list()

    def product(self):
        while True:
            with self.lock:
                i = random.randint(1,100000)
                self.custom_queue.append(i)
                print(f"product data: {i},size:{len(self.custom_queue)}")

            time.sleep(1)

    def consumer(self):
        while True:
            with self.lock:
                if len(self.custom_queue) >=1:
                    i = self.custom_queue.pop()
                    print(f"consumer data: {i},size:{len(self.custom_queue)}")
                else:
                    continue
                    print('no data to be consume')
            time.sleep(0.8)
    def main_run(self):
        product  = threading.Thread(target=self.product)
        consumer = threading.Thread(target=self.consumer)
        consumer.start()
        product.start()

if __name__ == '__main__':
    e1 = Example_1()
    e1.main_run()