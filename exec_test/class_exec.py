#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/9/13 20:32
# @Author:boyizhang
class Person2:
    def __init__(self, name, **kwargs):
        self.name = name


code_str = """  
# global_dict={}
class Person:  
    def __init__(self, name, **kwargs):  
        self.name = name  

p = Person(name='boyi111')  
total = 1  
def get_name():  
    print(total)  
    print(p.name)  
    p.name="hhhh"  
    print(p.name)  
    print('-'*100) 
print(p.name)
"""

global_dict = globals()
global_dict['p'] = Person2('boxy')
print(globals())

exec(code_str, global_dict, global_dict)
# global_dict['get_name']()
# print(globals())
exec('get_name()', global_dict)
