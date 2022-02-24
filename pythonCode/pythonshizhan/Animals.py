﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/2/24 22:19
# @Author: WZG
# @File: Animals.py

# 1.创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
# 2.创建子类【猫】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发 = 短毛，
# - 添加一个新的方法， 会捉老鼠，
# - 复写父类的‘【会叫】的方法，改成【喵喵叫】
# 3.创建子类【狗】，继承【动物类】，
# - 复写父类的__init__方法，继承父类的属性，
# - 添加一个新的属性，毛发 = 长毛，
# - 添加一个新的方法， 会看家，
# - 复写父类的【会叫】的方法，改成【汪汪叫】
# 4.创建一个猫猫实例
# - 调用捉老鼠的方法
# - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
# 5.创建一个狗狗实例
# - 调用【会看家】的方法
# - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
# 6.使用yaml来管理实例的属性


class Animals:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    @classmethod
    def shout(cls):
        print("Animals can shout!!!")

    @classmethod
    def run(cls):
        print("Animals can run!!!")


class Cat(Animals):
    def __init__(self, name, color, age, gender, hair="short"):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.hair = hair

    def catchRats(self):
        print("Cat can catch rats!!!")

    def shout(cls):
        print("Cat shout like miaomiao!!!")


mycat = Cat("Tom", "Orange", 3, "Famale")
mycat.shout()
