from random import *
import time
names=["pp","cp","hc","dp"]
subject=["java","python","aws"]
def student_list(num):
	record=[]
	for i in range(num):
		student={"id":i,"name":choice(names),"subject":choice(subjects)}
		record.append(student)
	return record

'''
def yy(num):
		for i in range(num):
		student={"id":i,"name":choice(names),"subject":choice(subjects)}
		yield student
'''
#l2=yy(1000)
#print(next(l2))
l1=student_list(10000)
t1=time.process_time()
print("time taken by l1 list is",t1)
