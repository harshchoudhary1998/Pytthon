# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:06:40 2019

@author: rj
"""

try:
    print("Inside outer block")
    try:
        print("inside inner block")
        a=int(input("enter the value"))
        b=int(input("enter the value"))
        print(a/b)
       # print(10/0)
    except ZeroDivisionError as e1:
        print("error is:",e1)
        print("inside except block")
except ValueError:
    print("hey")
    print("outside except block")