#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/17 17:46
# @Author:boyizhang
class FooParent(object):
    def __init__(self):
        print('Parent1-start')
        self.parent1 = 'parent1: I\'m the parent.'
        print('Parent1-end')

    def bar(self, message):
        print("%s from Parent" % message)


class FooParent2(object):
    def __init__(self):
        print('Parent2-start')
        self.parent2 = 'parent2: I\'m the parent.'
        print('Parent2-end')

    def bar(self, message):
        print("%s from Parent2" % message)


class FooChild(FooParent, FooParent2):

    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        # FooParent2.__init__(self)
        # FooParent.__init__(self)
        print('Child-start')
        super(FooChild, self).__init__()
        print('Child-end')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent1)


class A():
    def __init__(self):
        print('init A...')
        print('end A...')


class B(A):
    def __init__(self):
        print('init B...')
        super(B, self).__init__()
        print('end B...')


class C(A):
    def __init__(self):
        print('init C...')
        super(C, self).__init__()
        print('end C...')


class D(B, C):
    def __init__(self):
        print('init D...')
        super(D, self).__init__()
        print('end D...')


if __name__ == '__main__':
    fooChild = FooChild()
    # fooChild.bar('HelloWorld')
    # print(fooChild.parent1)
    D()
