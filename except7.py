# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:46:09 2019

@author: rj
"""

try:
    print("hey try")
    #print(10/0)
except:
    print("in except block")
    try:
        print("inisde except wala try block")
    except:
        print("except ke andar except")
    finally:
        print("Inside except wala finally")
finally:
    print("outer finally")
        