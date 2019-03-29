from functools import *
l1=[1,2,3,4,5,20000,5000]
l2=reduce(lambda a,b:a+b,l1)
print(l2)