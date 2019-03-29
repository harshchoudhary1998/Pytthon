# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:03:22 2019

@author: rj
"""

try:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    print(a/b)
except (ZeroDivisionError,ValueError) as e1:
    print("happened exception is",e1)