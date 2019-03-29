class inn:
	def __init__(self,name,age):
		self.age=age
		self.name=name
		print(id(self))
class cp(inn):
	def __init__(self,name,age,mobile):
		super().__init__(name,age)
		self.mobile=mobile
		print(id(self))
	def show(self):
		print(self.name,self.age,self.mobile)
a=cp("harsh","20","235454324")
a.show()