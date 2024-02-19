#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2021/10/10 11:40 上午
# @Author:boyizhang
from ObjectAndClass.animal import Animal, Animal2
from ObjectAndClass.cat import Cat, Cat2
from ObjectAndClass.dog import Dog

def test_animal(an: Animal):
    an.getVoice()

def test_animal2(an: Animal2):
    an.getVoice()


if __name__ == '__main__':
    ani = Animal("animal")
    dog = Dog("dog","red")
    cat = Cat("miaomiao")
    cat2 = Cat2('cat2')

    print(isinstance(ani,Dog))
    print(isinstance(dog,Dog))
    print(isinstance(dog,Animal))
    print(issubclass(Dog,Animal))
    print(dog.name)
    print(dog.color)

    print("-----cat------")
    print(f"catName: {cat.name}")
    cat.getVoice()
    cat.getLikeFood()

    print("-----cat end------")

    test_animal(ani)
    test_animal(dog)
    test_animal2(cat2)