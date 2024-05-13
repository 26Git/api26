#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/17 16:31
# Author     : pan
# @File     : xzs_login.py
# @Software : PyCharm
import requests

class xzs_login(object):
    def login(self,user,ps):
        self.url = "http://192.168.55.1:8000/api/user/login"
        self.header = {
            "Content-Type": "application/json"
        }
        self.data = {"userName":user,"password":ps,"remember":False}
        r = requests.post(url=self.url,headers=self.header,json=self.data)
        return r.text


if __name__ == '__main__':
    pass