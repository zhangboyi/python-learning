#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/24 16:01
# @Author:boyizhang

from multiprocessing.managers import BaseManager
from queue import Queue
queue = Queue()
class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue', callable=lambda:queue)
manager = QueueManager(address=('',9999),authkey=b'zby')

server = manager.get_server()
server.serve_forever()
while True:
    if not queue.empty():
        print(queue.get())

