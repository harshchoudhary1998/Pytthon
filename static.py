class static:
	a=99
	def __init__(self):
		self.a=88
a1=static()
print(a1.__dict__)
print("--------------------")
a1.a=12
print(a1.__dict__)
print("----------------------")
print("static variablr",static.a)