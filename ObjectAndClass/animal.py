#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/10 11:35 上午
# @Author:boyizhang



class Animal():
    def __init__(self,name):
        self.name = name

    def getVoice(self):
        print("I am a cue animal~")

import abc
class Animal2(metaclass=abc.ABCMeta):
    def __init__(self,name):
        self.name = name

    @abc.abstractmethod
    def getVoice(self):
        pass