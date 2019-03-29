# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:16:36 2019

@author: rj
"""

from threading import *
import time
e=Event()
def traffic():
    while True:
        time.sleep(10)
        print("now traffic police gives green signal")
        e.set()
        time.sleep(20)
        print("now police goving red signal")
        e.clear()
        
def driver():
    num=0
    while True:
        print("Driver wait for signal")
        e.wait()
        print("Traffic signmal is green")
        while e.isSet():
            num=num+1
            print("Vechile no",num,"crossing")
            time.sleep(2)
        print("traffic light red")
        
t1=Thread(target=traffic)
t2=Thread(target=driver)
t1.start()
t2.start()
        