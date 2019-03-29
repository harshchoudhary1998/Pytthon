class pp:
	a=9
	def __init__(self):
		self.b=80
	def m1(self):
		print("constructor of pp")
	@classmethod
	def m2(cls):
		print("class method")
	@staticmethod