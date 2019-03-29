class oops:
	def __init__(self,name,age,mobile):
		self.age=age
		self.name=name
		self.mobile=mobile
	def show(self):
		print("{} has {} age and number {}".format(self.age,self.name,self.mobile))
class oops2:
	@staticmethod      #ye hatane se error ayegi kyuki wo usse class lvl method smajega
	def display(a1):
		a1.age=a1.age-10
		a1.show()

a1=oops("hc",20,"987654312")
a2=oops2
a2.display(a1)