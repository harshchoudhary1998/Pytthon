# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:15:24 2019

@author: rj
"""

from threading import *
import time
def m1(num):
    for i in num:
        time.sleep(1)
        print("Cube is",i*i*i)
def m2(num):
    for i in num:
        time.sleep(1)
        print("square is",i*i)
        
starttime=time.time()
number=[1,2,3,4,5,6,7,8,9]
t1=Thread(target=m1,args=(number,))
t2=Thread(target=m2,args=(number,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Time elapsed is :",time.time()-starttime)