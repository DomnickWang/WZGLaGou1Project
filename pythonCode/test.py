#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/2/24 15:00
# @Author: WZG
# @File: test.py
import requests

# r = requests.get("http://www.baidu.com")
# r1 = requests.post('http://httpbin.org/post', data={'key': 'value'})
# r.encoding = "utf-8"

r = requests.get('https://api.github.com/events')
print(r.json())
