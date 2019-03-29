class inner1:
	def __init__(self):
		print("outer class constructor")
	class inner:
		def __init__(self):
			print("inner class")
a=inner1()
#del a error occur
#a2=inner()  error 
a2=a.inner()
#del a kardo koi farak nahi padna  
print(id(a),id(a2))
