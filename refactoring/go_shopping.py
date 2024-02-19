#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/6/17 09:06
# @Author:boyizhang
"""
让我们假设一下， 如果你想要购买一组运动装备， 比如一双鞋与一件衬衫这样由两种不同产品组合而成的套装。 相信你会想去购买同一品牌的商品， 这样商品之间能够互相搭配起来。
如果我们把这样的行为转换成代码的话， 帮助我们创建此类产品组的工具就是抽象工厂， 便于产品之间能够相互匹配。
1.工厂会生产鞋子与T恤(统一工厂的特性），如果工厂A生成裙子，工厂B不生产裙子
2.工厂有adidas 与 nike 或者更多
3.
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class ISportAbstract(ABC):
    @abstractmethod
    def make_shoe(self) -> IShoeAbstract:
        pass

    @abstractmethod
    def make_shirt(self) -> IShirtAbstract:
        pass

    @abstractmethod
    def make_skirt(self):
        raise Exception('需要自己实现')


class AdidasFactory(ISportAbstract):
    def make_skirt(self):
        pass

    # 具体的工厂
    def make_shoe(self):
        return AdidasShoe()

    def make_shirt(self):
        return AdidasShirt()


class NikeFactory(ISportAbstract):

    # 具体的工厂
    def make_shoe(self):
        pass

    def make_shirt(self):
        pass


class IShoeAbstract(ABC):
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def color(self):
        pass


class IShirtAbstract(ABC):
    @abstractmethod
    def price(self):
        pass


class AdidasShoe(IShoeAbstract):

    def price(self):
        return 100

    def color(self):
        return 'white'


class AdidasShirt(IShirtAbstract):
    def price(self):
        return 200


class NikeShoe(IShoeAbstract):
    def price(self):
        return 50

    def color(self):
        return 'black'


class NikeShirt(IShirtAbstract):
    def price(self):
        return 130


def client_code(factory: ISportAbstract):
    shirt = factory.make_shirt()
    shoe = factory.make_shoe()
    skirt = factory.make_skirt()

    print(shirt.price())
    print(shoe.price())


if __name__ == '__main__':
    client_code(AdidasFactory())
    client_code(NikeFactory())
    """
    使用animal与cat,dog 生成面向对象的应用
    
    """
