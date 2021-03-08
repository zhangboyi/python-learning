#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/3/7 9:20 下午
# @Author:boyizhang
# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from test_import.mypackage.Add import add

from .mypackage.Add import add



def ts_add():
    print(add(1, 3))


if __name__ == '__main__':
    print(add(1, 3))


