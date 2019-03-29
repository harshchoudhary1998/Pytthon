class static:
	a=99
	def __init__(self):
		del static.a
		static.b=23
	
	def m1(self):
		del static.b
		static.c=56

	@classmethod
	def m2():
		del static.c
		static.d=42

	@staticmethod
	def m3():
		del static.d
		static.f=12

a1=static()
print("-------------------after constructor-------------------")
print(static.__dict__)
print("-------------------after m1-------------------")
a1.m1()
print(static.__dict__)
print("-------------------after m2-------------------")
a1.m2()
print(static.__dict__)
print("-------------------after m3-------------------")
a1.m3()
print(static.__dict__)
