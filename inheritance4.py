class car:
	def __init__(self,name,model,color):
		self.name=name
		self.model=model
		self.color=color
	def getinfo(self):
		print("Car name {}\n Model no{} \n Color {}".format(self.name,self.model,self.color)

class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def eatdrinks(self):
		print("work hard")

class employee(person):
	def __init__(self,age,name,mobile,city,car):
		super().__init__(name,age)
		self.mobile=mobile
		self.city=city
		self.car=car
	def details(self):
		print("Employee name :",self.name)
		print("Employee Age :",self.age)
		print("Employee Mobile :",self.mobile)
		print("Employee City :",self.city)
		print("Employee Car :",self.car)
		self.car.getinfo() 

a2=car("Maruti","vdi","White")
a1=employee(35,"harsh",12343532,"jaipur",a2)
a1.detaisl()