#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/9/13 14:27
# @Author:boyizhang

# total=0
# def add(n, m):
#     global total
#     total +=1
#     sum = n + m
#     print("total:{total}")
#     return sum
# print(total)
# add(1,4)

code_str = """
total=0
def add2(n, m):
    global total
    total+=1
    sum = n + m
    print(f"total:{total}")
    
    return sum
    
print(globals())
"""


exec ("print('hhh')")
var_dict={}

exec(code_str)

# compile(code_str,'test.py',mode='exec')
# print(globals())
total1=10
code_str2 = """
# 优先级最高
# total1=10000
print(f"total1:{total1}")
"""

var_dict['total1'] = 11
exec(code_str2, var_dict, {'total1':90})

a = eval("add2(5,6)")
print(a)

print(eval("add2(19,100)"))
print(eval("add2(19,100)"))

exec("add2(19,100)")

exec("add2(19,100)")