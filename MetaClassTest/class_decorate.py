#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/7 11:38
# @Author:boyizhang
def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    print(obj)
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc
    aClass.ham = hamfunc
    return aClass


@Extender
class Client1():
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2

@Extender
class Client2():
    value = 'ni?'


c1 = Client1('Ni!')
print(c1.spam())
print(c1.eggs())
print(c1.ham('bacon'))

c2 = Client2()
print(c2.eggs())
print(c2.ham('bacon'))

