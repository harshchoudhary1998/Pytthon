class PP:
	def __init__(self,a,b):
		self.name=a
		self.age=b
	def display(self):
		self.c=200
		#del self.name delete the name attribute
		print("object initialize with {} and age {}".format(self.name,self.age))
		 
a1=PP("harsh",20)
print(a1.__dict__)
print("-------------------------")
a1.display()
print(a1.__dict__)
a1.e=900
print("_--------------------")
print(a1.__dict__)
del a1.e
print(a1.__dict__)