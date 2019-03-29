# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:42:59 2019

@author: rj
"""

from threading import *
import time
l=RLock()

def fact(n):
    l.acquire()
    result=0
    if n==1 or n==0:
        result=1
    else:
        result=n*fact(n-1)
    l.release()
    return result

def result(n):
    print("factorial is ",fact(n))
    
t1=Thread(target=result,args=(6,))
t2=Thread(target=result,args=(9,))
t1.start()
t2.start()