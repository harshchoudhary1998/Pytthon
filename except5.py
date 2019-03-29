# -*- coding: utf-8 -*-
"""12
Created on Mon Feb 11 17:21:44 2019

@author: rj
"""
'''try:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    print(a/b)
except ValueError as w:
    print("error is :",w)
finally:
    print("always run finally block")
'''
'''finally:
    print("ascsa")'''
import os
try:
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    print(a/b)
    os._exit(0)
except ValueError as w:
    print("error is :",w)
finally:
    print("always run finally block")