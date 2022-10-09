#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/21 21:29
# @Author:boyizhang
import multiprocessing
import os
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool


class Exmaple_1():

    def __init__(self, *args, **kwargs):
        pass
        # super(CLASS_NAME, self).__init__(*args, **kwargs)

    def task(self, n):
        print('%s is running' % os.getpid())
        time.sleep(2)
        return n * n

    def print_process_info(self):
        print(
            f'*******{multiprocessing.current_process().name}**********{multiprocessing.current_process().ident}*********')

    def main_run_apply_async(self):
        """
        进程池的用法
        :return:
        """
        with Pool(processes=4) as pool:  # start 4 worker processes
            print("----------------- apply -----------------")
            result = pool.apply(self.task, (10,))  # evaluate "f(10)" asynchronously in a single process
            print(result)
            print("----------------- apply_async -----------------")
            result = pool.apply_async(self.task, (10,))  # evaluate "f(10)" asynchronously in a single process
            print(result.get(timeout=2))  # prints "100" unless your computer is *very* slow
            print("----------------- map -----------------")
            print(pool.map(self.task, range(10)))  # prints "[0, 1, 4,..., 81]"
            print("----------------- imap -----------------")
            it = pool.imap(self.task, range(10))
            print(next(it))  # prints "0"
            print(next(it))  # prints "1"
            print(it.next(timeout=1))  # prints "4" unless your computer is *very* slow

            result = pool.apply_async(time.sleep, (10,))
            print(result.get(timeout=1))  # raises multiprocessing.TimeoutError


if __name__ == '__main__':
    e1 = Exmaple_1()
    p = ProcessPoolExecutor(max_workers=3,initializer=e1.print_process_info)
    l = []
    ctime = time.time()
    for i in range(10):
        obj = p.submit(e1.task, i)
        l.append(obj)

    p.shutdown()
    print('+' * 100)
    print([obj.result() for obj in l])
    # for item in l:
    # print(item.result())

    print(time.time() - ctime)

    # e1.main_run_apply_async()
