# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:41:19 2019

@author: rj
"""

from threading import *
import time
def show():
    print(current_thread().getName(),"...started")
    time.sleep(2)
    print(current_thread().getName(),"..ended")
    
print("Total active threda",active_count())
t1=Thread(target=show,name="pp1")
t2=Thread(target=show,name="pp2")
t1.start()
t2.start()

l=enumerate()
for i in l:
    print("thread name:",i.name)
    
time.sleep(5)
print("---------Now again list out Thread--------")
l=enumerate()
for i in l:
    print("Thread name :",i.name)