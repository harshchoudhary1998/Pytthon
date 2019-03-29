# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:50:25 2019

@author: rj
"""

'''from zipfile  import *
f=ZipFile("hc.zip",'w',ZIP_DEFLATED)
print(type(f))
f.write("hc.txt")
f.write("abc.txt")
f.close()
print("Zip file created successfully")'''





from zipfile  import *
f=ZipFile("hc.zip",'r',ZIP_STORED)
print(type(f))
name=f.namelist()
for i in name:
    print("file name->",i)
    f1=open(i,"r")
    print(f1.read())
f.close()
print("UnZip file created successfully")




