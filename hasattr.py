class A:
	def m1(self):
		print("asfdasfswe")
class B:
	def m2(self):
		print("Bgvjhv")
def f1(object):
	if (hasattr(object,"m1")):
		object.m1()
	else:
		object.m2()

a1=A()
f1(a1)
b1=B()
f1(b1)


