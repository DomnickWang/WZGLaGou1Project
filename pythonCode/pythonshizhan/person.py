#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/2/24 16:52
# @Author: WZG
# @File: person.py

class Person:
    name: str = "default"
    gender: str = "default"
    age: int = 20
    money: float = 1000.0

    def __init__(self, name, gender, age, money):
        self.name = name
        self.gender = gender
        self.age = age
        self.money = money
        print("end init")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

    def make_money(self):
        print(f"{self.name} coule make money")


p = Person("Tom", "Male", 25, 20000.00)
p.eat()
p.sleep()
p.run()
p.make_money()


class FunnyMan(Person):
    pass


f = FunnyMan("Mike", "Male", 27, 30000.00)
