#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/5/6 10:44 AM
# @Author:boyizhang


#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0
total=0
e = queue.Queue()

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        # process_data(self.name, self.q)
        add_list(self.name)
        print ("退出线程：" + self.name)

def add_list(num):
    global e
    e.put(num)

def process_data(threadName, q):
    global total
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            total+=data
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2","Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five","Six"]
queueLock = threading.Lock()
workQueue = queue.Queue()
threads = []
threadID = 1

# 创建新线程
for tName in range(10):
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()

queueLock.acquire()
for num in range(100):
    workQueue.put(num)
queueLock.release()

# 等待队列清空
# while not workQueue.empty():
#     pass

# 通知线程是时候退出
exitFlag = 1
print("-"*80)
print(e.queue)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
print(total)