# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:59:43 2019

@author: rj
"""

from threading import *
import time
def m1():
    for i in range(5):
        print("THREAD NATURE",current_thread().isDaemon())
        time.sleep(3)
        
t=Thread(target=m1)
print(t.isDaemon())
t.setDaemon(True)
t.start()
print("Inside main non daemon thread")