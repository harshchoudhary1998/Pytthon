# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:28:30 2019

@author: rj
"""

from threading import *
import time
def show():
    print(current_thread().getName,"...started")
    time.sleep(3)
    print(current_thread().getName,"...ended")
    
print("Total Active threads",active_count())
t1=Thread(target=show,name="pp1")
t2=Thread(target=show,name="pp2")
t1.start()
t2.start()
print("The number of active thread :",active_count())
time.sleep(5)
print("The number of active thread :",active_count())