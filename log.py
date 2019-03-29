# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:54:09 2019

@author: rj
"""

'''from logging import *
debug("debug info")
warning("compile info")
error("error info")'''



'''from logging import *
basicConfig(filename="logfile.txt",level=WARNING) #is level ke upar wale level sare print ho jayega
debug("debug info")
warning("compile info")
error("error info")
critical("critical error info")
info("basic info")
f=open("logfile.txt","r")
print("now the data is stored successfully")
for i in f:
    print(i)
f.close()'''



'''from logging import *
basicConfig(format="%(asctime)s :%(levelname)s :%(message)s",datefmt="%d/%y/%m %H :%M :%S :%P") #format he
debug("debug info")
warning("compile info")
error("error info")
critical("critical error info")
info("basic info")'''

from logging import *
basicConfig(filename="logfile.txt",format="%(asctime)s :%(levelname)s :%(message)s",datefmt="%d/%y/%m %H :%M :%S :%P")
info("a new request info")
try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    print("Result is:",a/b)
except zerodivisionerror:
    
                                    















