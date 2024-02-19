#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2023/6/17 09:04
# @Author:boyizhang

"""
logistics:road/sea/sky
transport: car/truck/ship/plane

"""
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def plan_delivery(self):
        pass

    @abstractmethod
    def create_transport(self):
        pass


class RoadLogistics(Logistics):

    def plan_delivery(self):
        pass

    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):

    def plan_delivery(self):
        pass

    def create_transport(self):
        return Ship()


class Transport(ABC):
    @abstractmethod
    def delivery(self):
        pass


class Truck(Transport):
    def delivery(self):
        print("使用火车运输")


class RoadTransport(Transport):
    def delivery(self):
        pass


class Car(Transport):
    def delivery(self):
        print("使用小轿车运输")


class Plane(Transport):
    def delivery(self):
        print("使用Plane运输")


class Ship(Transport):
    def delivery(self):
        print("使用Ship运输")

def client():
    pass
