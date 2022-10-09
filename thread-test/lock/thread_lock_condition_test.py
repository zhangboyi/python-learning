#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/23 11:32
# @Author:boyizhang
import random
import threading
import time
from threading import Condition
from queue import Queue


class Example_1():

    def __init__(self):
        self.con = Condition()
        self.queue = Queue()

    def product(self):
        while True:
            with self.con:

                i = random.randint(1,100)
                self.queue.put(i)
                print(f"product:{i},queue.size:{self.queue.qsize()}")
                print("product done.")
                time.sleep(1)
                self.con.notify()
                self.con.wait()

    def consumer(self):
        while True:
            with self.con:
                self.con.wait()
                # print(f"queue.size:{self.queue.qsize()}")
                print(f"[consumer]:{self.queue.get()},queue.size:{self.queue.qsize()}")
                print("consumer done.")
                time.sleep(1)
                self.con.notify()
    def main_run(self):

        product = threading.Thread(target=self.product)
        consumer = threading.Thread(target=self.consumer)

        # consumer 先执行
        consumer.start()
        product.start()




if __name__ == '__main__':
    example_1 = Example_1()
    example_1.main_run()