def decor(f1):
	def inner(x,y):
		print("we are divide {} with {}".format(x,y))
		if y==0:
			print("hey enter valid value")
			return
		else:
			f1(x,y)
	return inner
@decor
def div(a,b):
	print("division is :",a/b)

div(10,2)
div(4,0)