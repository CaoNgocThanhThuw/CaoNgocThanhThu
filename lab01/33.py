# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:48:18 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
import math
n = int(input("Nhập vào số nguyên dương n: "))
if n > 0:
    can_bac_2 = math.sqrt(n)  
    if can_bac_2 ** 2 == n:
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")
else:
    print("Số nhập vào không phải là số nguyên dương.")