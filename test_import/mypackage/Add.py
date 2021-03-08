#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/3/7 9:20 下午
# @Author:boyizhang

# from .mypackage import Add
from ..mypackage.Sub import sub
from .testmypack.Div import div


def add(n1: object, n2: object) -> object:
    return n1 + n2


print('sub:', sub(5, 7))

print('div:', div(4,5))
