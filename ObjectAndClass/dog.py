#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/10 11:37 上午
# @Author:boyizhang
from ObjectAndClass.animal import Animal


class Dog(Animal) :
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getVoice(self):
        print("旺旺~")