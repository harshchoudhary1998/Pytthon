# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:56:12 2019

@author: rj
"""

'''f=open("hrc.txt","w")
print(type(f))
print(f.name)
print(f.mode)
f.close()'''


'''f=open("hc.txt","a")
f.write("HELLO\n")
f.write("FRIENDS\n")
f.write("CHAI PEELO\n")
print("writing data successfully\n")
f.close()
f=open("hc.txt","r")
data=f.read(122)
print(data)
f.close()'''



'''f=open("hc.txt","a")
list=["Harsh\n","Choudhary\n"]
f.writelines(list)
print("writing data successfully\n")
f.close()
f=open("hc.txt","r")
data=f.read(122)
print(data)
f.close()'''




'''f=open("hc.txt","r")
line=f.readline()
print(line,end='--')
line2=f.readline()
print(line2)
f.close()
print("*************")
f=open("hc.txt","r")
lines=f.readlines()
print(type(lines))
for line in lines:
    print(line,end='--')
    
f.close()'''




'''with open("hc.txt","a") as f:
    f.write("why")
    print("file is closed")'''
    
    

'''f=open("hc.txt","r")  #agar read kar rahe ho to close na karne me error nahi ayegi
print(f.tell())
print(f.read(4))
print("---------")
print(f.tell())
print(f.read())'''


'''data="hows you I am Harsh from Skit"
f=open("abc.txt","w")
f.write(data)
print("Write data successfully")
with open("abc.txt","r+") as f:
    text=f.read()
    print(text)
    print("current position",f.tell())
    f.seek(8)
    print("current position",f.tell())
    f.write("Coder of Skit:")        sara replace nahi hoga run kar
    f.seek(0)
    text=f.read()
    print("modification is",text)'''
    
 

    
'''f=open("hc.txt","r+")
d=f.readlines()
print(type(d))
f.seek(0)
for i in d:
    if i=="harsh\n":       #last character \n he yaad rakho bhai
        f.write(i.replace("harsh","HC"))
    else:
        f.write(i)
        
f.truncate()
f.close()


f=open("hc.txt","r+")
d=f.readlines()
for i in d:
    print(i,end="")
f.close()'''




'''import sys,os
f=input("enter file path")
if os.path.isfile(f):
    print("file exists",f)
    f1=open(f,"r")
else:
    print("file not exists")
    sys.exit()
#f1=open("hc.txt","r")  
lcount=ccount=wcount=0
for l in f1:
    lcount=lcount+1
    ccount=ccount+len(l)
    words=l.split()
    print(type(words))
    wcount=wcount+len(words)
print("No of lines",lcount)
print("No of characters",ccount)
print("No of words",wcount)'''
     
    


f1=open("F:\my diaries\ashwin birthday and amer diaries2017//IMG-20170108-WA0009 - Copy - Copy.jpg","rb")
bytes=f1.read()
f2=open("hc.jpg","wb")
f2.write(bytes)










































































































