class oops:
	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name
	def setMarks(self,marks):
		self.marks=marks
	def getMarks(self):
		return self.marks
s=oops()
s.setName(input("enter the name."))
s.setMarks(int(input("enter the marks")))
print("{} and {}".format(s.getName(),s.getMarks()))