#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/7 11:30
# @Author:boyizhang

class Client1():
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2():
    value = 'ni?'


def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


Client1.eggs = eggsfunc
Client1.ham = hamfunc

Client2.eggs = eggsfunc
Client2.ham = hamfunc

c1 = Client1('Ni!')
print(c1.spam())
print(c1.eggs())
print(c1.ham('bacon'))

c2 = Client2()
print(c2.eggs())
print(c2.ham('bacon'))
