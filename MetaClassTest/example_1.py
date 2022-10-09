#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/7 14:42
# @Author:boyizhang

def Trace(classname,supers,classdict):
    aClass = type(classname,supers,classdict)
    class Wrapper():
        
        def __init__(self, *args, **kwargs):
            self
            
