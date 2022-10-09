#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/9/18 14:20
# @Author:boyizhang
import time
import atexit

@atexit.register
def my_clean():
    print('my clean')

def main_run():

    while True:
        print("hhhhh")
        time.sleep(1)


if __name__ == '__main__':
    main_run()