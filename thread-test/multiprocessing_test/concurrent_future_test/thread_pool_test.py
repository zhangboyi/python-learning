#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/24 18:31
# @Author:boyizhang
import concurrent.futures
import math
import multiprocessing
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# from multiprocessing.sharedctypes import Array
from multiprocessing import Array


class Example_1():

    def __init__(self, *args, **kwargs):
        self.add_list = list()
        self.PRIMES = [
            112272535095293,
            112582705942171,
            112272535095293,
            115280095190773,
            115797848077099,
            1099726899285419]
        # self.add_list_lock = Array('c', '', lock=Lock())
        # self.temp = Array('i', [1, 2, 3, 4])
        # self.queue = queue.Queue()

    def run(self, n):
        time.sleep(1)
        self.add_list.append(n)
        print(f'{n}-{self.add_list}-{len(self.add_list)}')
        return f'{n},{self.add_list}'

    def run_by_process(self, n,item=None):
        print("hhhhh")
        time.sleep(1)
        # self.queue.put(n)
        # with self.add_list_lock:
        #     self.add_list_lock.value += str(n)
        #     print(f'{n}-{self.add_list_lock}-{len(self.add_list_lock)}')
        # print(f'{n},{item.qsize()}')
        # return f'{n},{item.qsize()}'

    def is_prime(self, n):
        time.sleep(1)
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True

    def print_thread_info(self):
        print(f'*******{threading.currentThread().name}**********')

    def print_process_info(self):
        print(
            f'*******{multiprocessing.current_process().name}**********{multiprocessing.current_process().ident}*********')

    def main_run_thread_pool(self):
        executor = ThreadPoolExecutor(max_workers=10, thread_name_prefix='BoXiaoYi', initializer=self.print_thread_info)

        with executor as e:
            future_list = [e.submit(self.run, i) for i in range(100)]
            print(f"future_list:{future_list}")
            for item in concurrent.futures.as_completed((future_list)):
                try:
                    data = item.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (item, exc))
                else:
                    print('%r page is %d bytes' % (item, len(data)))

    def main_run_thread_pool_map(self):
        executor = ThreadPoolExecutor(max_workers=10, thread_name_prefix='BoXiaoYi', initializer=self.print_thread_info)

        with executor as e:
            return_list = e.map(self.run, range(100))
            print(f"return_list:{return_list}")
            for item in return_list:
                print('%r page is %d bytes' % (item, len(item)))

    def main_run_process_pool(self):
        """
        todo problem
        :return:
        """
        # temp = Array('i', [1, 2, 3, 4])
        # ctx = multiprocessing.get_context('spawn')
        # q = ctx.Queue()
        q=None
        executor = ProcessPoolExecutor(max_workers=5, initializer=self.print_process_info)
        with executor as e:
            future_list = [e.submit(self.run_by_process, i,q) for i in range(10)]
            # future_list = e.map(self.run, range(10))

            print(f"future_list:{future_list}")
            print([obj.result(timeout=1) for obj in future_list])
            # for item in concurrent.futures.as_completed(future_list):
            #     try:
            #         data = item.result()
            #     except Exception as e:
            #         print(e)
            #     else:
            #         print('%r page is %d bytes' % (item, len(data)))

        # p = ProcessPoolExecutor()  # 不填则默认为cpu的个数
        # l = []
        # start = time.time()
        # for i in range(10):
        #     obj = p.submit(self.run_by_process, i)  # submit()方法返回的是一个future实例，要得到结果需要用obj.result()
        #     l.append(obj)
        # print(l)
        #
        # p.shutdown()  # 类似用from multiprocessing import Pool实现进程池中的close及join一起的作用
        # print('=' * 30)
        # # print([obj for obj in l])
        # print([obj.result() for obj in l])
        # print(time.time() - start)

    def main_run_process_pool_2(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            result_list = executor.map(self.is_prime, range(100))
            print(f'result_list:{result_list}')
            for number, prime in zip(range(100), result_list):
                print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    e1 = Example_1()
    # e1.main_run_thread_pool()
    # e1.main_run_process_pool_2()
    e1.main_run_process_pool()
    # e1.main_run_thread_pool_map()
    print(e1.add_list)
