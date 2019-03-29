class inn:
	a=300
	def __init__(self):
		self.b=90
	def show(self):
		print(self.a,self.b,"inn")
class hc:
	def __init__(self):
		self.inh=inn()
	def desplay(self):
		print(self.inh.a)
		self.inh.show()
a1=hc()
a1.desplay()