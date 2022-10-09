#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/10 3:31 下午
# @Author:boyizhang


def test_Number():
    print("-------Number start-------")
    # 定义一个整数
    num = 888
    output(id(num),type(num))
    # 修改该整数
    num = 999
    output(id(num),type(num))
    print("-------Number end-------")

def test_Str():
    print("-------Str start-------")
    # 定义一个str
    str1 = "hello"
    output(id(str1),type(str1))
    # 修改str
    str1 = "hello world!"
    output(id(str1), type(str1))

    print("-------Str end-------")

def test_Tuple():
    print("-------tuple start-------")
    l = [1,2,3]
    # 定义一个tupple
    t1 = (l,5,6)
    output(id(t1),type(t1))
    # 修改str
    l.append(9)
    output(id(t1), type(t1))

    print("-------tuple end-------")

def test_list():
    print("-------list start-------")
    l1 = [1,2,3]
    list
    output(id(l1),type(l1))
    # 修改list
    l1.append(9)
    output(id(l1), type(l1))
    l1[0] = 2
    output(id(l1), type(l1))
    l1.remove(2)
    output(id(l1), type(l1))

    print("-------list end-------")

def test_dict():
    d1 = dict()
    d1["a"] = '1'
    d1["b"] = '2'
    print(d1.get("a"))
    print(d1["b"])

    # key不存在会返回None或者默认值
    print(d1.get("c",0))
    # key不存在会报KeyError
    # print(d1["c"])

    for key,val in d1.items():
        print(f"key:{key},value:{val}")

    for d in d1.keys():
        print(d)
        print(d1.get(d))
    for d in d1.values():
        print(d)


    d2 = dict()
    d2["a"] = [1,2,3]
    d2["b"] = 2
    print(type(d2.get("a")))
    print(d2.get('a'))
    d2.get("a").append(111)
    d2["b"] = d2.get("b")+1
    print(d2.get('a'))

    d3 = d2.copy()
    print(str(d3))
    if d3.get('d') is None:
        d3.setdefault("d",1)
    print(d3)

    d3.update(d1)
    print(d3)

def output(id,type):
    print(f"内存地址：{id},数据类型：{type}")

# def output(value):
#     print(f"内存地址：{id(value)},数据类型：{type(value)}")


if __name__ == '__main__':
    # test_Number()
    #
    # test_Str()
    #
    # test_Tuple()
    #
    # test_list()

    test_dict()