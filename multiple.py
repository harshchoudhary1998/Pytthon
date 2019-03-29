class A:
	def m1(self):
		print("inside A")
class B(A):
	def m1(self):
		print("inside B")
class C(A):
	def m1(self):
		print("inside C")
class D(B,C,A):
	pass

a1=D()
a1.m1()
print(A.mro())
print(B.mro())
print(C.mro())
