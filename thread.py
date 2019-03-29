# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:14:26 2019

@author: rj
"""

from threading import *

'''print("hey hows you")
print("Current thread is :",current_thread().getName())'''






'''def display():
    for i in range(1,11):
        print("Child thread----->",current_thread().getName())
        
#t=Thread(target=display())isse naya thread nahi banega
t=Thread(target=display)
t.start()
for i in range(1,5):
     print("Main thread----->",current_thread().getName())'''
     
     
     
     
     
     
'''class pp(Thread):
    def run(self):
        for i in range(1,10):
            print("child thread")
            
t=pp()
t.start()
for i in range(1,4):
    print("Main Thread")
    
print("Total Active count",active_count())'''



'''def show(slef):
	print("This is show thread")
	for i in range(5):
		print("Run Show Thread",current_thread().getName())
def show2(slef):
	print("This is show thread")
	for i in range(2):
		print("Run Show Thread",current_thread().getName())


a1=pp()
t=Thread(target=a1.show)
t.start()
t=Thread(target-a1.show2)
t.start()
for i in range(10):
	print("Main thread",current_thread().getName())'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


















