class PP:
	bc=90
	@staticmethod
	def m1(a,b):
		print("addition is",a+b)

	@staticmethod
	def m2(a,b):
		print("multiplication",a*b,PP.bc)

a1=PP()
a1.m1(8,9)
a1.m2(2,5)