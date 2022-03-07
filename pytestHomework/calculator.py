#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/3/7 19:06
# @Author: WZG
# @File: calculator.py
class Calculator:

    def add(self, a, b):
        return a + b

    def cut(self, a, b):
        return a - b

    def ride(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print("被除数不能为0")
        else:
            return a / b
