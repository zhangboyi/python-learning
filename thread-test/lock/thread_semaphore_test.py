#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/23 12:16
# @Author:boyizhang
import threading
import time


class BoundedSemaphore_Example_1():

    def __init__(self, *args, **kwargs):
        self.semaphore = threading.BoundedSemaphore(5)
        self.sem = threading.Semaphore()

    def run(self, n):
        # ways-1
        # self.semaphore.acquire()
        # print("active_thread: %d, run the thread-%s: %s" % (threading.active_count(), str(threading.get_ident()), n))
        # time.sleep(2)
        # self.semaphore.release()

        # ways-2
        with self.semaphore:
            print(
                "active_thread: %d, run the thread-%s: %s" % (threading.active_count(), str(threading.get_ident()), n))

            time.sleep(2)

    def sem_run(self, n):

        with self.semaphore:
            print(
                "active_thread: %d, run the thread-%s: %s" % (threading.active_count(), str(threading.get_ident()), n))

            time.sleep(2)

    def main_run(self):
        # 设置允许5个线程同时运行
        # print_thread = threading.Thread(target=self.print_thread_info)
        # print_thread.start()
        thread_list = []
        for i in range(20):
            t = threading.Thread(target=self.run, args=(i,))
            thread_list.append(t)
            t.start()
            # t.run()
        # for item in thread_list:
        #     item.join()

    def sem_main_run(self):
        for i in range(20):
            t = threading.Thread(target=self.sem_run, args=(i,))
            t.start()

    def print_thread_info(self):
        while True:
            print('-' * 100)
            print(f"active_thread:{threading.active_count()}")
            print(f"active_get_ident:{threading.get_ident()}")
            print(f"active_enumerate:{threading.enumerate()}")
            print(f"active_main_thread:{threading.main_thread()}")
            print('-' * 100)
            time.sleep(1)


class Semaphore_Example_1():
    pass


if __name__ == '__main__':
    """
    Semaphore与BoundedSemaphore的区别是调用release()方法的处理:
    每释放一个信号量（每条用一次release()方法），将内部计数器的值增加1。
    BoundedSemaphore在调用release()方法的时候，先判断内部计数器的值是否大于初始值。如果大于或者等于初始值的话,将会引发 ValueError 异常。
    如果小于初始值的话，处理方式与Semaphore一致。
    """
    e1 = BoundedSemaphore_Example_1()
    # e1.main_run()
    e1.sem_main_run()
    print(f"I'm main thread-{threading.get_ident()}-{threading.main_thread()}.")
