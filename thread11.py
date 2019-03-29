# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:33:54 2019

@author: rj
"""

from threading import *
l=RLock()
print("Main Thread trying to acquire lock")
l.acquire()
print("Main Thread again trying to acquire lock")
l.acquire()