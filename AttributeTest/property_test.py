#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/10 23:51
# @Author:boyizhang
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        pass


# p = Person(name='boyi',age = 20)
# p.n

class Animal():

    def getName(self): ...

    def setName(self): ...


class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(obj.dirname)


class Directory:
    size = DirectorySize()  # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname  # Regular instance attribute


if __name__ == '__main__':
    # 描述器
    s = Directory('songs')
    g = Directory('gaes')
    print(s.size)
    print(g.size)
    # property
    p = Person(name='boyi', age=20)
    p.name = 'bo'
    print(p.name)

    animal = Animal()
    print(animal.getName())
