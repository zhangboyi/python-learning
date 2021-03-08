#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/3/8 8:56 下午
# @Author:boyizhang
import sys, os
# 当前模块的位置：/Users/boyizhang/PycharmProjects/demo/test_import/mypackage/testabspath.py
print(__file__)
# 返回当前模块的绝对路径：/Users/boyizhang/PycharmProjects/demo/test_import/mypackage/testabspath.py
print(os.path.abspath(__file__))
#  当前模块的绝对路径目录：/Users/boyizhang/PycharmProjects/demo/test_import/mypackage
print(os.path.dirname(os.path.abspath(__file__)))
# 返回当前模块目录的上层目录，每多一层，即再上一层目录：/Users/boyizhang/PycharmProjects/demo/test_import
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 当前模块的真实地址: /Users/boyizhang/PycharmProjects/demo/test_import/mypackage/testabspath.py
print(os.path.realpath(__file__))
# 当前文件夹的路径: /Users/boyizhang/PycharmProjects/demo/test_import/mypackage
print(os.path.dirname(os.path.realpath(__file__)))
path = os.path.dirname(os.path.abspath(__file__))
# 将目录或路径加入搜索路径
sys.path.append(path)


print(__name__)


