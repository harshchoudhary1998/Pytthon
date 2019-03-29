class pp:
	head=1
	def m1(self):
		self.a=10
	@classmethod
	def run(cls,name,feet):
		print("{} run with {} feet ".format(name,feet))
a1=pp()
a1.run("dog",4)