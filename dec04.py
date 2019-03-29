def decor2(f1):
	def inner():
		print("executed inside decor2")
	return inner

def decor1(f1):
	def inner():
		print("executed inside decor1")
	return inner

@decor2
@decor1
def pp():
	print("inside pp")

pp()