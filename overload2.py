class emp:
	def __init__(self,name,salary):
		self.name=name
		self.salary=salary
	def __mul__(self,other):
		return self.salary*other.day

class ts:
	def __init__(self,day):
		self.day=day

a=emp("harsh",12000)
t=ts(2)
print(a*t)
print(8*7)