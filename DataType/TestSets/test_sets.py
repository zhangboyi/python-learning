#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/7/17 16:23
# @Author:boyizhang

set1 = {"apple", "banana", "cherry"}
set2 = {'orange'}
set1.add('watermelon')
print(set1)
set1.update(set2)
print(set1)
set1.remove('banana')
print(set1)
set3=set1.intersection(set2)
print(f'set1: {set1}, set3: {set3}')

set3=set1.symmetric_difference(set2)
print(f'set1: {set1}, set3: {set3}')

set3 = set1.difference(set2)
print(f'set1: {set1}, set3: {set3}')
set1.intersection_update(set2)
print(set1)
