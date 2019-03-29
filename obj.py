class pp:
	def __init__(self,name,age): #agar constructor me self ke jagah kuch or bhi likhoge to chalega we usse hamesh self he samjega
		self.a=name
		self.b=age
	def show(self):
		print("Name is {} and age is{}".format(self.a,self.b))

a1=pp("harsh",60)
a1.show()