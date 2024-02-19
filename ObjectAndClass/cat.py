#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/10 11:50 上午
# @Author:boyizhang
from ObjectAndClass.animal import Animal, Animal2


class Cat(Animal):

    def getVoice(self):
        print(f"{self.name}:miao~")

    def getLikeFood(self):
        print("I like fish~")

class Cat2(Animal2):
    def getVoice(self):
        print("I am cat2~")

