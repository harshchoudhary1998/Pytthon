class pp:
	def __init__(self):
		self.a=34
	def m1(self):
		print("instance member",self.a)

class cp(pp):
	def m2(self):
		print("child method")
a1=cp()
a1.m1()
a1.m2()