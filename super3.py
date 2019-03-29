class A:
	def m1(self):
		print("A class ")

class B(A):
	def m1(self):
		print("B class ")

class C(B):
	def m1(self):
		print("C class ")

class D(C):
	def m1(self):
		print("D class ")

class E(D,A):
	def m1(self):
		super(D,self).m1()
		C.m1(self)
		B.m1(self)
		print("D class ")

a1=E()
a1.m1()