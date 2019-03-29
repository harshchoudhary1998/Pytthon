# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:04:44 2019

@author: rj
"""

from threading import *
import time
def producer():
    time.sleep(2)
    print("producer thread producing items")
    print("producer thread gives notification")
    event.set()
    
def consumer():
    print("consumer thread waiting to consume item")
    event.wait()
    print("now consumer thread consuming the item")
    
event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()