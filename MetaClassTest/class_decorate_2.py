#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/7 14:44
# @Author:boyizhang

def Trace(aClass):
    class Wrapper():

        def __init__(self, *args, **kwargs):
            self.wrapper = aClass(*args, **kwargs)

        def __getattr__(self, item):
            print(f"Trace:{item}")
            return getattr(self.wrapper, item)

    return Wrapper


@Trace
class Person():

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


def TraceMeta(classname, supers, classdict):
    """
    - 首先，它必须使用一个简单的函数而不是一个类，因为type子类必须附加给对象创建协议。
    - 其次，必须通过手动调用type来手动创建主体类；它需要返回一个实例包装器，但是元类也负责创建和返回主体类
    :param classname:
    :param supers:
    :param classdict:
    :return:
    """
    aClass = type(classname, supers, classdict)

    class Wrapper():
        def __init__(self, *args, **kwargs):
            self.wrapper = aClass(*args, **kwargs)

        def __getattr__(self, item):
            print(f"Trace:{item}")
            return getattr(self.wrapper, item)

    return Wrapper


class PersonMeta(metaclass=TraceMeta):

    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


if __name__ == '__main__':
    boyi = Person('boyi', 40, 50)
    print(boyi.name)
    print(boyi.pay())
    person_meta = PersonMeta('boyi', 40, 50)

    print(person_meta.name)
    print(person_meta.pay())
