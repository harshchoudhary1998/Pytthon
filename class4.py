class hc:
	c=90
	e=10
	def __init__(self,a,b):
		hc.f="harsh"  #static variable inside constructor
		self.a=a
		self.b=b
		print(hc.f,self.f) #access static variable if you write f then you will get error
	def show(self):
		hc.k="chocho" # static variable inside instance variable
		print(self.a,self.b)
	
a1=hc(20,30)
a1.show()
a1.d=1000
print(a1.__dict__)
print("--------------------")
a2=hc(10090,2080)
a2.show()
print(a2.__dict__)
print("---------------------------")
a1.a=433
print(a1.__dict__)
print(a1.c)