# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:22:44 2019

@author: rj
"""

from threading import *
print(current_thread().getName())
current_thread().setName("HARSH")
print(current_thread().getName())
print(current_thread().name)
print(current_thread().ident)
