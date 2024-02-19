#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/6/17 08:42
# @Author:boyizhang
from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class AbstractProductA(ABC):
    @abstractmethod
    def function_a(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def function_b(self):
        pass

    @abstractmethod
    def other(self, collaborator: AbstractProductA):
        pass


class ConcreteProductA(AbstractProductA):
    def function_a(self):
        print('create product a....')
        return 'product a'


class ConcreteProductA2(AbstractProductA):
    def function_a(self):
        print('create product a2')
        return 'product a2'


class ConcreteProductB(AbstractProductB):

    def other(self, collaborator: AbstractProductA):
        result = collaborator.function_a()

        return f"The result of the B2 collaborating with the ({result})"

    def function_b(self):
        print('create function b.....')
        return 'product b'


class ConcreteProductB2(AbstractProductB):

    def other(self, collaborator: AbstractProductA):
        result = collaborator.function_a()

        return f"The result of the B2 collaborating with the ({result})"

    def function_b(self):
        print('create function b2.....')
        return 'product b2'


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"{product_b.function_b()}")
    print(f"{product_b.other(product_a)}", end="")


if __name__ == '__main__':
    client_code(ConcreteFactory1())
    print('\n')
    client_code(ConcreteFactory2())
