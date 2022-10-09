#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   decorate.py
@Time    :   2022/05/08 14:19:45
@Author  :   boyi.zhang 
@Version :   1.0
@Contact :   boyi.zhang@shopee.com
@License :   (C)Copyright 2020-2022, ZhangBoyi
@Desc    :   None
'''

# here put the import lib
import time

def load_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'actual excution time is {time.perf_counter()-t1}')
        return res
    return wrapper