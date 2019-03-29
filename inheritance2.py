class inn:
	a=45
	def m1(self):
		print("inside inn class m1 meyhod")
	@classmethod
	def m2(cls):             #def m1(cls) doge to error nahi ayega but last wala call hoga
		cls.b=9
		print("Inside m2")
	@staticmethod
	def m3():
		print("Inside m2")

class cp(inn):
	pass
a1=cp()
a1.m1()
a1.m2()
a1.m3()

