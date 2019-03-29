class pp:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def display(self):
		print(self.name,self.age)

class pp1(pp):
	def __init__(self,name,age,branch):
		#self.age=90  gazab maza ayega
		super().__init__(name,age)
		#self.age=90 yaha likne se anarth ho jayega
		self.branch=branch
	def show(self):
		super().display()
		print(self.branch)
a1=pp1("Harsh",20,"cse")
a1.show()