#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/3/7 19:18
# @Author: WZG
# @File: test_cal.py
import pytest
import yaml


def getdatas():
    with open("./data.yml", encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
    return datas


@pytest.mark.parametrize('a,b', getdatas())
class Testcal:
    @pytest.mark.add
    def test_add(self, calculate, a, b):
        print("加法测试")
        assert a + b == calculate.add(a, b)
        print(f"{a} + {b} = {calculate.add(a, b)}")

    @pytest.mark.cut
    def test_cut(self, calculate, a, b):
        print("减法测试")
        assert a - b == calculate.cut(a, b)
        print(f"{a} - {b} = {calculate.cut(a, b)}")

    @pytest.mark.ride
    def test_ride(self, calculate, a, b):
        print("乘法测试")
        assert a * b == calculate.ride(a, b)
        print(f"{a} * {b} = {calculate.ride(a, b)}")

    @pytest.mark.div
    def test_div(self, calculate, a, b):
        print("除法测试")
        if b == 0:
            print("被除数不能为0")
        else:
            assert a / b == calculate.div(a, b)
            print(f"{a} / {b} = {calculate.div(a, b)}")
