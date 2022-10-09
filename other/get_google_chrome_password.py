#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/28 12:52
# @Author:boyizhang

# 查看谷歌浏览器保存在本地的密码

import os
import shutil
import sqlite3

# try:
#     import win32crypt
# except ImportError as e:
#     os.popen('pip install pywin32')
#     import win32crypt

db_file_path = os.path.join('/Users/boyizhang/Desktop/Login Data For Account')

tmp_file = os.path.join('/Users/boyizhang/Desktop', 'sqlite_file-2')
print(tmp_file)
if os.path.exists(tmp_file):
    os.remove(tmp_file)
shutil.copyfile(db_file_path, tmp_file)

conn = sqlite3.connect(tmp_file)
for row in conn.execute('select signon_realm,username_value,password_value from logins'):
# for row in conn.execute('select * from logins'):
    print(row)
    # print(f"{row[0]} - {row[1]}  -  {bytes.decode(row[2],encoding='gbk')}")
    # ret = win32crypt.CryptUnprotectData(row[2], None, None, None, 0)
    # print('网站：%-50s，用户名：%-20s，密码：%s' % (row[0][:50], row[1], row[2].decode('utf-8')))

conn.close()
# os.remove(tmp_file)
