#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024/2/19 18:16
# @Author:boyizhang


import random, string

def gen_random_string(length):
    # 数字的个数随机产生
    num_of_numeric = random.randint(1,length-1)
    # 剩下的都是字母
    num_of_letter = length - num_of_numeric
    # 随机生成数字
    numerics = [random.choice(string.digits) for i in range(num_of_numeric)]
    # 随机生成字母
    letters = [random.choice(string.ascii_letters) for i in range(num_of_letter)]
    # 结合两者
    all_chars = numerics + letters
    # 洗牌
    random.shuffle(all_chars)
    # 生成最终字符串
    result = ''.join([i for i in all_chars])
    return result


print(gen_random_string(40))