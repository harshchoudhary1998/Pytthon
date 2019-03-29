class inner2:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show(self):
		print("{} and age is {}".format(self.name,self.age))
	class inner:
		def __init__(self,mobile):
			self.mobile=mobile
		def display(self):
			print(self.mobile)
a1=inner2("Tannush",6)
a1.show()
a1.inner("978307723").display()
print(a1.__dict__)


    
