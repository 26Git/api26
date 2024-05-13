#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:44
# Author    : ping
# @File     : send_email_base.py
# @Software : PyCharm
# 用于建立smtp连接
import smtplib
# 邮件需要专门的MIME格式
from email.mime.text import MIMEText
# plain指着普通文件格式邮件内容
msg = MIMEText("邮件内容","plain","utf-8")
# 发件人
msg['From']='2871586386@qq.com'
# 收件人
msg['To']='2871586386@qq.com'
# 邮件的标题
msg['Subject']='接口测试报告主题'
smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('2871586386@qq.com','gntnjfujmhjhdded')
smtp.sendmail('2871586386@qq.com','2871586386@qq.com',msg.as_string())
smtp.quit()
