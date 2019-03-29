# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:49:24 2019

@author: rj
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:42:59 2019

@author: rj
"""

from threading import *
import time
s=Semaphore(2) #koi two thread ayegi bake sarri wait karegi but jo two thread ayegi wo random chalegi

def st(n):
    s.acquire()
    s.acquire() #dikkat ho jayegi
    for i in range(10):
        print("this is critical section thread",end="-->")
        time.sleep(1)
        print(n)
    s.release()
    s.release()
    
t1=Thread(target=st,args=("hc",))     #COMA se turple form me convert ho jata he
t2=Thread(target=st,args=("cc",))
t3=Thread(target=st,args=("we",))
t1.start()
t2.start()
t3.start()