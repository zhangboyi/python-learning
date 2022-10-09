#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/10 11:50 上午
# @Author:boyizhang
from ObjectAndClass.animal import Animal


class Cat(Animal):

    def getVoice(self, name):
        print(f"{name}:miao~")

    def getLikeFood(self):
        print("I like fish~")
