#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   thread_test.py
@Time    :   2022/05/08 10:29:12
@Author  :   boyi.zhang 
@Version :   1.0
@Contact :   boyi.zhang@shopee.com
@License :   (C)Copyright 2020-2022, ZhangBoyi
@Desc    :   None
'''

# here put the import lib
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

balance = 0
class UserAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print('{} deposit {},balance is {}'.format(self.name, amount,self.balance))

    
    def withdraw(self, amount):
        if self.balance >= amount:
            
            self.balance -= amount
            print('{} withdraw {},balance is {}'.format(self.name, amount,self.balance))
        else:
            print('Not enough money. balance is {}'.format(self.balance))
    def deposit2(self, amount):
        global balance
        balance += amount
        print('{} deposit {},balance is {}'.format(self.name, amount,balance))

    
    def withdraw2(self, amount):
        global balance
        balance -= amount
        print('{} withdraw {},balance is {}'.format(self.name, amount,balance))

    def run_thread_by_type(self, type, amount):
        if type == 'deposit':
            for i in range(100):
                self.deposit(amount)
        if type == 'withdraw':
            for i in range(100):
                self.withdraw(amount)
    def run_thread(self, amount):

        for i in range(100000):
            self.deposit2(amount)
            self.withdraw2(amount)

def calculate(i):
    print(i)
    return i
if __name__ == '__main__':
    user = UserAccount('zhang', 0)
    # t1 = threading.Thread(target=user.run_thread_by_type, args=('deposit',100))
    # t2 = threading.Thread(target=user.run_thread_by_type, args=('withdraw',200))
    # t3 = threading.Thread(target=user.run_thread_by_type, args=('withdraw',100))


    # t1 = threading.Thread(target=user.run_thread, args=(100,))
    # t2 = threading.Thread(target=user.run_thread, args=(300,))
    # t3 = threading.Thread(target=user.run_thread, args=(200,))
    # t1.start()
    # # t2.start()
    # t3.start()
    # t1.join()
    # # t2.join()
    # t3.join()
    # print(user.balance)
    # print(balance)



    with ThreadPoolExecutor(3) as executor:
        Futures = [executor.submit(calculate, i) for i in range(13)]
    res = []
    for r in as_completed(Futures):
        res.append(r.result())
    print(res)

    