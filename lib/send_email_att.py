#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 9:31
# Author    : ping
# @File     : send_email_att.py
# @Software : PyCharm
# 用于建立smtp连接
import smtplib
# 邮件需要专门的MIME格式
from email.mime.text import MIMEText
# 支持附件
from email.mime.multipart import MIMEMultipart
# 用于使用中文邮件主题
from email.header import Header
# 读取report的内容 放到变量email_body中
with open('../report/report.html', encoding='utf-8')as f:
    email_body=f.read()


# plain指着普通文件格式邮件内容
# msg = MIMEText("邮件内容","plain","utf-8")
msg = MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
# 发件人
msg['From']='2871586386@qq.com'
# 收件人
msg['To']='2871586386@qq.com'
# 邮件的标题
msg['Subject']=Header('接口测试报告主题','utf-8')

# 上传附件
# 构造附件1，传送当前目录下的report.html文件
att1 = MIMEText(open('../report/report.html', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="report.html"'
msg.attach(att1)

# 建立连接
smtp = smtplib.SMTP_SSL('smtp.qq.com')
# 登录
smtp.login('2871586386@qq.com','gntnjfujmhjhdded')
# 发送邮件
smtp.sendmail('2871586386@qq.com','2871586386@qq.com',msg.as_string())
smtp.quit()
