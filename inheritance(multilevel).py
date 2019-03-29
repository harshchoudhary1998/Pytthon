class pp:
	def __init__(self):
		self.a=34
	def m1(self):
		print("instance member",self.a)

class cp(pp):
	def m2(self):
		print("child method")

class dp(cp):
	pass
a1=dp()
a1.m1()
a1.m2()