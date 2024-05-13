#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/28 14:33
# Author    : ping
# @File     : send_email.py
# @Software : PyCharm
# 用于建立smtp连接
import logging
import smtplib
# 邮件需要专门的MIME格式
from email.mime.text import MIMEText
# 支持附件
from email.mime.multipart import MIMEMultipart
# 用于使用中文邮件主题
from email.header import Header
from config.config import *

def send_email(report_file):

    # 读取report的内容 放到变量email_body中
    with open(report_file,encoding='utf-8')as f:
        email_body=f.read()


    # plain指着普通文件格式邮件内容
    # msg = MIMEText("邮件内容","plain","utf-8")
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body,'html','utf-8'))
    # 发件人
    msg['From']=sender
    # 收件人
    msg['To']=receiver
    # 邮件的标题
    msg['Subject']=Header(subject,'utf-8')

    # 上传附件
    # 构造附件1，传送当前目录下的report.html文件
    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)
    try:
        # 建立连接
        smtp = smtplib.SMTP_SSL(smtp_server)
        # 登录
        smtp.login(smtp_user,smtp_ps)
        # 发送邮件
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info("====================发送邮件成功======================")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email('../report/report.html')