# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:11:42 2019

@author: rj
"""

import os
'''print(os.getcwd())'''



'''os.mkdir("hc/hacm")          #phele hc banna hua chaiye fir he hacm banega otherwise error ayrgi
print("directory created")'''


'''os.makedirs("hc/hacm")'''

#os.rmdir("hc/hacm")  #sirf last wali delete hogi but pura address path specify karna jaruri he

#os.removedirs("hc/hacm")


#print(os.listdir("."))


for dir,dirname,filename in os.walk("."):
    print("directory :",dir)
    print("path",dirname)
    print("file",filename)
    print("------------------------")































