# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:07:19 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập số lượng số hạng n: "))
tong = 0
for i in range(n + 1):
    mau = 2 * i + 1
    tong += 1 / mau
print("Tổng của dãy số là:", tong)
