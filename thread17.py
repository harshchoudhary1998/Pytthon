# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:27:55 2019

@author: rj
"""

from threading import *
import random
import time

items=[]

def consumer():
    while True:
        c.aquire()
        print("Consumer waiting for updation")
        c.wait()
        print("consumer got notification",items.pop(item))
        c.release()
        time.sleep(3)
        
def producer():
    while True:
        
         c.aquire()
         item=random.randint(1,200)
         print("producer producing item",item)
         items.append(item)
         print("producer gives notification")
         c.notify()
         c.release()
         time.sleep(3)
         
c=condition()
t1=Thread(target=consumer)
t2=Thread(target=producer)
t1.start()
t2.start()
   