def hc(f1):
	print(type(f1))
	def inner():
		print("i am inner")
		f1()
	def inne2r():
		print("i am inner2")
		f1()
	return inner

@hc
def m1():
	print("inside outer")

m1()