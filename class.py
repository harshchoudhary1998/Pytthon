class hc:
	"""MY NAME IS KHAN
	AND I AM NOT A TERRORIST"""
	a=90
	b=70
	def m1(self):
		self.e=10
		self.f=99
		print("inside m1()")
	def m2(self):
		self.c=10
		self.d=99
		print("inside m2()")
	def __init__(self):
		print("constructor")
a1=hc()
print(hc.__doc__)
print(hc.__dict__)
print("------------------")
a1.m1()
print(a1.__dict__)
print("--------------------")
a1.m2()
print(a1.__dict__)
