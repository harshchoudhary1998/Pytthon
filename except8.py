# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:59:30 2019

@author: rj
"""

class pp1(Exception):
    def __init__(self,msg):
        self.msg=msg
        
a1=input("Enter name")
if a1=="HARSH":
    raise pp1("pp1 customize exception")
   # print("asdsad")
else:
    print("No exception")