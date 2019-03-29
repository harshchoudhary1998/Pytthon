# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:56:33 2019

@author: rj
"""

from threading import *
s=BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
print("working")