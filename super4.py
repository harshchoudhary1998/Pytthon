class pp:
	a=9
	def __init__(self):
		self.b=80
	def m1(self):
		print("constructor of pp")
	@classmethod
	def m2(cls):
		print("class method")
	@staticmethod
	def m3():
		print("static method")

class cp(pp):
	a=90
	def __init__(self):
		super().__init__()
		self.b=100
		print(super().a)
		print(self.a)
		super().m2()
		super().m3()
	def c(self):
		super().__init__()
		self.b=100
		print(super().a)
		print(self.a)
		super().m2()
		super().m3()

'''	@classmethod
	def c(self):
		super().__init__()
		self.b=100
		print(super().a)          bhaisahab error ayegi
		print(self.a)             1.__init__()-->positional argument missing he
		super().m2()              2. __init__(self)-->nameerror means sekf is not defined
		super().m3()'''

a=cp()
print("------------")
a.c()