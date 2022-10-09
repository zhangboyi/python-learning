#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/7 12:36 AM
# @Author:boyizhang
import queue
import random
import time

import gevent
from gevent import monkey
from gevent.pool import Pool,Group

monkey.patch_all()
total = 0
queue_result = queue.Queue()
def load_time(func):
    def wrapper(*args,**kwargs):
        ctime = int(time.time())
        result = func(*args,**kwargs)
        mtime = int(time.time())
        print(f'call %s(), load time is {mtime-ctime} ms' % func.__name__)
        return result
    return wrapper
def calculate(num):
    print(f"--input num:{num}--")
    queue_result.put(num)
    sleep_time = random.randint(0,2)
    print(f"##sleep time:{sleep_time}s##")
    time.sleep(sleep_time)

@load_time
def single_thread():
    for i in range(100):
        calculate(num=i)

@load_time
def mul_thread():
    tasks=[]
    for i in range(100):
        tasks.append(gevent.spawn(calculate,i))
    # gevent.joinall(tasks)

@load_time
def mul_thread_pool():
    pool = Pool(10)
    tasks=[]
    pool.start(gevent.greenlet)
    for i in range(100):
        tasks.append(pool.spawn(calculate,i))
    # gevent.joinall(tasks)
    pool.kill()
@load_time
def mul_thread_group():
    group = Group()
    # group.apply()
    tasks=[]
    for i in range(100):
        tasks.append(group.apply_async(calculate,(i,)))
    # gevent.joinall(tasks)
    group.join()

# @load_time
def mul_thread_while():
    left = 0
    batch_size = 10
    j = 0
    total_len=1000
    sqls = []
    for i in range(total_len):
        sqls.append(i)
    while left < total_len:
        group = Group()
        right = left + batch_size
        print(f"run: left:{left}-right:{right}")
        if right > total_len:
            right = total_len
        tasks = [group.spawn(calculate, sql) for i, sql in
                 enumerate(sqls[left:right])]
        print(gevent.getcurrent())
        # gevent.joinall(tasks)
        group.join()

        left = right
        j += 1

def get_num(num):
    return num
def group_test1():
    g1 = Group()
    for i in range(10):
        result = g1.map(get_num,(i,))
    for i in result:
        print(i)

if __name__ == '__main__':
    # single_thread()
    mul_thread()
    # mul_thread_pool()
    # mul_thread_group()
    # mul_thread_while()
    # group_test1()
    time.sleep(3)
    while not queue_result.empty():
        total+=queue_result.get()

    print(total)
