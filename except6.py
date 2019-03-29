# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:40:11 2019

@author: rj
"""

 try:
     
     print("inside inner block")
     a=int(input("enter the value"))
     b=int(input("enter the value"))
     print(a/b)
     
except ZeroDivisionError:
     print("gjjj")
    
else:
    print('ho gaya bhai")
    
finally:
    print("inside finally")