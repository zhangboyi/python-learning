#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/3/25 10:49
# @Author:boyizhang
from typing import Dict,MutableMapping
from collections import Counter


def populate_ranks(votes: Dict[int, str], ranks: Dict[int, str]):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i
    # return ranks


def get_winner(ranks):
    return next(iter(ranks))


# from collections.abc import MutableMapping


class SortedDict(MutableMapping[str,int]):

    def __init__(self, *args, **kwargs):
        self.data = {}

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


def test_dict():
    ranks = {}
    votes = {
        "by": 123,
        "boyi": 9999999,
        "boxy": 12312,

    }
    populate_ranks(votes, ranks)

    print(ranks)

    winner = get_winner(ranks)
    print(winner)
    for i in iter(ranks):
        print(i)


def test_sort_dict():
    ranks = SortedDict()
    votes = {
        "by": 123,
        "boyi": 9999999,
        "boxy": 12312,

    }
    populate_ranks(votes, ranks)

    print(ranks)

    winner = get_winner(ranks)
    print(winner)
    # for i in iter(ranks):
    #     print(i)


def test_counter():
    b = Counter("chenkc")  # string

class Visit():
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value
    def __getitem__(self, item):
        return self.data[item]
def test_visit():
    visit = Visit()
    print(visit.data)
    visit.boxy = 123
    print(visit.data)
    print(visit.boxy)

def open_picture(key):
    pass
class Picture(dict):
    def __missing__(self, key):
        raise Exception("jjjj")

def test_pictrure():
    p = Picture()
    p['c']



if __name__ == '__main__':
    test_sort_dict()
