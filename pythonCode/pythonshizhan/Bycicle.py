#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/2/24 17:34
# @Author: WZG
# @File: Bicycle.py

class Bycicle:
    def run(self, km):
        print(f"骑行的里程数为： {km}")


class EBycicle(Bycicle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        print(f"充电： {vol}")

    def run(self, km):
        e_mile = self.battery_level * 10
        ride_mile = km - e_mile

        if ride_mile > 0:
            print(f"电动行驶里程：{e_mile} km")
            # 调用父类的run()方法
            super().run(ride_mile)
        else:
            print(f"电动行驶里程：{km} km")


myebycicle = EBycicle(10)
myebycicle.run(35)
