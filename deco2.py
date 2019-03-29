def decor(f1):
	def hc(ff):
		print("hello ji")

	return hc


@decor
def wish(name):
	print("ByR BUR")

wish("harsh")