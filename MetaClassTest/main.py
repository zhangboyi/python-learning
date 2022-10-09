#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/6 14:00
# @Author:boyizhang

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ',classname, supers, classdict, sep='----')

    return type(classname, supers, classdict)

class Eggs:
    pass

print('making class')

class Spam(Eggs,metaclass=MetaFunc):
    data = 1
    def meth(self,args):
        pass


print('making instance')

x = Spam()

print(f'data: {x.data}')