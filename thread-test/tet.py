#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/23 11:52
# @Author:boyizhang
import threading
import time
con = threading.Condition()
def run():
    while 1:
        with con:
            # 使用上下文管理器，省去了自动上锁解锁的过程
            print('-----------------')
            print('我完事了，该你了')
            con.notify()
            # 发起一个信号，释放掉一个wait
            con.wait()


def result():
    while 1:
        with con:
            con.wait()
            # 我在等待一个noity出现，这样我就能运行了
            time.sleep(0.3)
            print('三秒后....')
            print('我也完事了，你继续')
            con.notify()

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=result)
t2.start()
t1.start()
# 注意这里必须t2先运行，想想为什么
