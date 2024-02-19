#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024/2/19 17:29
# @Author:boyizhang
import bisect
import collections
import random

l = []
for i in range(10):
    n = random.randint(1,100)
    bisect.insort(l,n)
    print(f"n:{n}, l:{l}")
print(l)

# l = [123,12,3,990]
# bisect.bisect(l)
random.shuffle(l)
print(l)
l2 = random.choices(['red', 'black', 'green'], [18, 5, 2], k=20)
print(l2)

deck = collections.Counter(tens=16, low_cards=36)
print(deck)
seen = random.sample(list(deck.elements()), k=10)
print(seen)
