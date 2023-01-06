#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/17 18:08
# @Author:boyizhang
class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p1 = People('波小艺', 20)
    p2 = People('啵啵', 23)
    print("userName: {1.name}, age: {0.age}".format(p1, p2))
    # print("userName: {name}, age: {age}".format_map(p1))
    info = {"name": "python教程", "Author": "波小艺"}
    # name: python教程, Author: 波小艺
    print("name: {name}, Author:{Author}".format(**info))
    # print("name: {name}, Author:{Author}".format(info))
    print("name: {name}, Author:{Author}".format_map(info))
