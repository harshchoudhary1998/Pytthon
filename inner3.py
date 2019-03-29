import gc
class inner3:
	def __init__(self):
		print("--Object Initialization--")
	class inner2:
		def m1(self):
			print("inner class m1")
	class inner:
		def m2(self):
			print("inner class m2")

a1=inner3()
a1.inner2().m1()
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
