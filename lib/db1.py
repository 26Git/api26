#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 16:03
# Author    : ping
# @File     : db.py
# @Software : PyCharm
import logging

import pymysql
from config.config import *
# 获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=db_host,
    port=db_port,
    user=db_user,
    passwd=db_ps,
    db=db,
    charset='utf8')
    return conn
# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()#获取连接
    cur = conn.cursor()#建立游标
    logging.debug(sql)
    cur.execute(sql)#执行sql
    result = cur.fetchall()#获取所有查询结果
    logging.debug(result)
    cur.close()#关闭游标
    conn.close()#关闭连接
    return  result#返回结果
# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()#获取连接
    cur = conn.cursor()#建立游标
    try:
        cur.execute(sql)#执行sql
        logging.debug(sql)
        conn.commit()#提交更改
    except Exception as e:
        logging.error(str(e))
        conn.rollback()#回滚
    finally:
        cur.close()#关闭游标
        conn.close()#关闭游标
# 封装常用数据库操作
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from t_user where user_name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False
def add_user(name,password):
    spl = "insert into t_user (user_name,password) value ('{}','{}')".format(name,password)
    change_db(spl)
def del_user(name):
    sql = "delete from t_user where user_name='{}'".format(name)
    change_db(sql)