# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:17:14 2019

@author: rj
"""

'''def m1():
    print("asdsad")
print(callable(m1))
a=9*8
print(callable(a))'''

class pp:
    def __call__(self):
        print("I am bck")
a=pp()
print(callable(a))
