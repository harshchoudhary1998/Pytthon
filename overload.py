class hc:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):
		print(id(self))
		return self.pages*other.pages
a=hc(80)
b=hc(60)
print(id(a))
c=9+8
print(c)
print(a+b)