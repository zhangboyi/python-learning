#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/24 10:20
# @Author:boyizhang
import multiprocessing as mp
import os
import threading
import time
from multiprocessing import Pool, Process


class Example_1():
    def __init__(self):
        self.my_arr = [i for i in range(1, 10)]

    def hello_world(self):
        t = threading.currentThread()
        time.sleep(1)
        print(f'thread_name: {t.name}: hello world')

    def foo(self, q):
        q.put('hello')

    def print_process_info(self):
        print(f'module name: {__name__}')
        print(f'parent process id: {os.getppid()}')
        print(f'process id: {os.getpid()}')

    def operate_queue(self, q: mp.Queue):
        q.put(['hello', 'boyi'])

    def pipe_test(self, conn: mp.Pipe):
        conn.send(['hello', 'boyi', 'and pipe'])
        conn.close()

    def main_run_proccess_share(self):
        # mp.set_start_method('spawn')
        # q = mp.Queue()
        # p = mp.Process(target=self.foo, args=(q,))
        # p.start()
        # print(q.get())
        # p.join()

        ctx = mp.get_context('spawn')
        q = ctx.Queue()
        p = ctx.Process(target=self.foo, args=(q,))
        p.start()
        print(q.get())
        p.join()

    def proccess_share_memory(self, num, arr):
        num.value = 3.1415927
        print(
            f"proccess_share_memory:{arr}-{mp.current_process().pid}-{os.getpid()}")
        for i in range(len(arr)):
            arr[i] = -arr[i]
            # self.my_arr[i] = -arr[i]

        # 各个进程之间数据是隔离的，在该进程内self.my_arr内的元素均为负数,但回到主进程后，self.my_arr内的元素依然保持为整数
        # 所以需要使用共享内存(Value/Array)或者服务器进程(Manager())共享数据。
        # 进行并发编程时，通常最好尽量避免使用共享状态。使用多个进程时尤其如此。
        # print(f"proccess_share_memory:{self.my_arr}")

    def main_run_proccess(self):
        """
        Process 类
        :return:
        """
        # self.print_process_info()
        p = Process(target=self.hello_world)
        self.print_process_info()
        p.start()
        p.join()

    def main_run_process_spawn_queue(self):
        """"
        Queue() 类
        """
        mp.set_start_method('spawn')
        q = mp.Queue()
        p = mp.Process(target=self.operate_queue, args=(q,))
        p.start()
        print(q.get())
        p.join()

    def main_run_process_pipe(self):
        """
        Pipe() 函数返回一个由管道连接的连接对象，默认情况下是双工（双向）。
        :return:
        """
        p_conn, c_conn = mp.Pipe()
        p = Process(target=self.pipe_test, args=(c_conn,))
        print(p_conn.recv())
        p.start()
        p.join()

    def main_run_proccess_share_memory(self):
        """
        Process 类 之共享内存
        :return:
        """
        num = mp.Value('d', 0.0)
        arr = mp.Array('i', range(10))
        print(f'pid:{os.getpid()}')
        p = Process(target=self.proccess_share_memory, args=(num, self.my_arr))
        p.start()
        p.join()
        print(num.value)
        print(arr[:])
        print(self.my_arr[:])

    def main_run_pool(self):
        """
        进程池
        :return:
        """
        with Pool(5) as p:
            p.map(self.hello_world)

    def main_run_process_fork(self):
        pass

    def main_run_process_forkserver(self):
        pass


if __name__ == '__main__':
    e1 = Example_1()
    # e1.main_run_process()
    # e1.main_run_proccess()
    e1.main_run_proccess_share_memory()
    # e1.main_run_process_spawn()
    # e1.main_run_process_pipe()
    # e1.print_process_info()
    print(
        f'main_thread: {threading.main_thread()} - {threading.currentThread().name}')
