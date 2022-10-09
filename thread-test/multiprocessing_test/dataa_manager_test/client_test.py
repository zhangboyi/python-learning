#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/24 16:03
# @Author:boyizhang
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
m = QueueManager(address=('127.0.0.1', 9999), authkey=b'zby')
m.connect()
queue = m.get_queue()
queue.put('hello boyi')