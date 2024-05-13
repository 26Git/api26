#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:18
# Author    : ping
# @File     : 带参数的get请求.py
# @Software : PyCharm
import requests

# 方法一:参数直接在url中
# url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"

# 方法二：参数在字典里面
url = "http://www.tuling123.com/openapi/api"

pama={
    "key":"ec961279f453459b9248f0aeb6600bbe",
    "info":'你好'
}

r = requests.get(url,params=pama)

print(r.text)

