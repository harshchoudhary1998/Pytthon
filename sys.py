import sys
class dest2:
	pass
t1=dest2()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))