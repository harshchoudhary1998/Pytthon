# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:08:41 2019

@author: rj
"""

from threading import *
import time
#import ctypes
l=Lock()
def m1(name):
    
    l.acquire()
    for i in range(3):
        print("Good eveneing",end=' ')
        time.sleep(2)
        print(name)
    l.release()
t1=Thread(target=m1,args=("HC",))
t2=Thread(target=m1,args=("HACM",))    
t3=Thread(target=m1,args=("CHOCHO",))  
t1.start()
t2.start()
t3.start()      
        
        
        
        
'''l=Lock()
l.acquire()
l.release()'''
    