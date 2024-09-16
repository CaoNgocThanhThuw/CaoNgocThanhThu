# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:08:31 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập số lượng số hạng n: "))
tong = 0
for i in range(1, n + 1):
    mau = 2 * i
    tong += 1 / mau
print("Tổng của dãy số là:", tong)
