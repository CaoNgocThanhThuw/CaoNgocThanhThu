# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:09:16 2024

@author: Cao Ngọc Thanh Thư 23719291
"""
email = input("Nhập vào địa chỉ email để kiểm tra: ")
ten_mien_hop_le = {'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'}
if '@' in email and '.' in email:
    username, domain = email.rsplit('@', 1)
    if len(username) >= 6:
        if domain in ten_mien_hop_le:
            print(f"{email} là địa chỉ email hợp lệ.")
        else:
            print(f"{email} không phải là địa chỉ email hợp lệ.")
    else:
        print(f"{email} không phải là địa chỉ email hợp lệ.")
else:
    print(f"{email} không phải là địa chỉ email hợp lệ.")
