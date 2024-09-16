# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:06:05 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số lượng số hạng n: "))
tong = 0
mau = 0
for i in range(1, n + 1):
    mau += i
    tong += x ** i / mau
print("Tổng của dãy số là:", tong)
