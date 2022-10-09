#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/7 17:01
# @Author:boyizhang
import time


def trace(func):
    calls = 0

    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s '%(calls,func.__name__))
        return func(*args, **kwargs)

    return onCall


def timer(label='', trace=True):
    def onDecorator(func):
        def onCall(*args, **kwargs):
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f,%.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
                return result

        onCall.alltime = 0
        return onCall

    return onDecorator


class Person():
    @trace
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @trace
    def giveRaise(self,percent):
        self.pay += (1.0 + percent)
    @trace
    def firstName(self):
        return self.name.split()[0]

if __name__ == '__main__':
    boyi = Person('boyi zhang',50000)
    boxy = Person('boxy zhang',100000)
    print(boyi.name,boxy.name)
    boxy.giveRaise(0.1)
    print(boxy.pay)
    print(boyi.firstName(),boxy.firstName())

