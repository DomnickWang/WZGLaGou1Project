#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/3/7 19:18
# @Author: WZG
# @File: conftest.py
import pytest
from pytestHomework.calculator import Calculator


@pytest.fixture()
def calculate():
    cal = Calculator()
    print("开始计算")
    yield cal
    print("结束计算")
