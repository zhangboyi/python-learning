#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/6 10:25 AM
# @Author:boyizhang

import threading
from time import sleep, ctime

N = 100  # 100张票

lock = threading.Lock()

def LockSell(name):

   global N

   while True:

       lock.acquire()
       try:
          if N>0:
           sleep(0.1)  #加入此句，可以让线程卖出第0张票或同一张票
           print("{}卖出第{}张票！\n".format(name,N))
           N=N-1
       finally:
           # 改完了一定要释放锁:
           lock.release()
def NoLockSell(name):
   global N

   while True:
       if N>0:
          sleep(0.1)  #加入此句，可以让线程卖出第0张票或同一张票
          print("{}卖出第{}张票！\n".format(name,N))
          N=N-1
def main():

  threads = {}

  for i in ( "A" ,"B"  ):
      # 实例化每个 Thread 对象，把函数和参数传递进去，返回 Thread 实例
      t = threading.Thread(target=LockSell, args=( i  ,))
      # t = threading.Thread(target=NoLockSell, args=( i  ,))
      threads[i]=t     # 分配线程

  for i in  ("A" ,"B"):
      threads[i].start()    # 开始执行多线程

  for i in  ("A" ,"B"):
      threads[i].join()     # 等待线程结束或超时，然后再往下执行

  print("程序结束！")


if __name__ == '__main__':
  main()