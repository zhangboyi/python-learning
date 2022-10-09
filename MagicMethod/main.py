#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/17 23:05
# @Author:boyizhang

class People(object):
    # 创建对象
    def __new__(cls, *args, **kwargs):
        print("触发了构造方法")
        ret = super().__new__(cls)  # 调用父类的__new__()方法创建对象
        return ret  ## 将对象返

    # 实例化对象
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化方法")

    #  删除对象
    #   del 对象名或者程序执行结束之后
    def __del__(self):
        print("析构方法，删除对象")
    def __call__(self, *args, **kwargs):
        print('call() ')
        return args


# -*- coding: UTF-8 -*-

class Meter(object):
   """
   对于单位"米"的描述器
   """
   def __init__(self, value=0.0):
       self.value = float(value)

   def __get__(self, instance, owner):
       return self.value

   def __set__(self, instance, value):
       self.value = float(value)

class Foot(object):
   """
   对于单位"英尺"的描述器
   """
   def __get__(self, instance, owner):
       return instance.meter * 3.2808
   def __set__(self, instance, value):
       instance.meter = float(value) / 3.2808

class Distance(object):
   """
   用米和英寸来表示两个描述器之间的距离
   """
   meter = Meter(10)
   foot = Foot()

if __name__ == '__main__':
    p1 = People('xiaoming', 16)
    print(p1.age)
    print(p1((1,2,3)))

    d = Distance()
    print(d.foot)
    print(d.meter)



# 输出：
# 触发了构造方法
# 初始化方法
# 析构方法，删除对象