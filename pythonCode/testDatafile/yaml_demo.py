#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/2/24 15:55
# @Author: WZG
# @File: yaml_demo.py
import yaml

# print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))
with open("demo3.yml", "w") as f:
    yaml.dump({'a': [1, 2]}, stream=f)
