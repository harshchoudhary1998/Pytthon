# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:46:22 2019

@author: rj
"""

try:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    print(a/b)
except ZeroDivisionError as e1:
    print("happened exception is",e1)
    
except ValueError as e1:
    print("happened exception is",e1)
except:
    print("safsac")