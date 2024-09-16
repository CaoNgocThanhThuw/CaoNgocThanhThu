# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:04:01 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
n = int(input("Nhập số lượng số hạng n: "))
tong = 0
for i in range(1, n + 1):
    tu = 2 * i - 1
    mau = 2 * i
    tong += tu / mau
print("Tổng của dãy số là:", tong)
