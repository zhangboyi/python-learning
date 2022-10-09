#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/4/6 8:15 下午
# @Author:boyizhang


def func(x):
    return x+1

age_list = [4,13,20,23]
age_list2 = [8,13,20,23]
# [5, 14, 21, 24]
print(list(map(func, age_list)))
print(list(map(lambda x: x * 2, age_list)))

def get_even(num):
    if num%2==0:
        return True
print(list(filter(get_even, age_list)))
print(list(filter(lambda x:x>14,age_list)))

from functools import reduce
def do_sum(x,y):
    return x+y
print(reduce(do_sum, age_list))
print(reduce(lambda x,y:x+2*y, age_list))

name = ['小红','小明','小华','小窝']
nas = zip(name,age_list)
# ('小红', 4) ('小明', 13) ('小华', 20) ('小窝', 23)
for n in nas:
    print(n, end=' ')

print()
# enumerate
for key,val in enumerate(name, start= 1):
    print(key,val,end='|')
print()
print(dict(enumerate(name, start=1)))

for i in range(5):
    # 0 1 2 3 4
    print(i,end=' ')
for i in range(2,5):
    # 2 3 4
    print(i,end=' ')
for i in range(0,5,2):
    # 0 2 4
    print(i,end=' ')