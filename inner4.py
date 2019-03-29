class inner4:
	def __init__(self):
		self.name="pratipal"
		self.age=self.Age()
		self.branch=self.Branch()
	def display(self):
		print("name :",self.name)
		self.age.m1()
		self.branch.m2()
	class Age:
		def __init__(self):
			print("------------Inside Age Class--------")
		def m1(self):
			print("----------Your ade is 30-----------")
	class Branch:
		def __init__(self):
			print("--------------Inside Branch class--------")
		def m2(self):
			print("--------------your branch is CSE----------")
a1=inner4()
a1.display()