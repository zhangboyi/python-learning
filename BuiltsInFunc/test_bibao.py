#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/3/26 20:30
# @Author:boyizhang

def sort_priority(values, group):
    is_found = False
    def helper(x):
        nonlocal is_found
        if x in group:
            print(f'x:{x}')
            is_found = True
            return (0, x)
        return (1, x)

    print(f'values:{values}')
    # 使用返回的元组进行比较大小
    values.sort(key=helper)
    print(f'is_found:{is_found}')


def test_sort_priority():
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = [5, 3, 2, 7]
    sort_priority(numbers, group)
    print(numbers)
