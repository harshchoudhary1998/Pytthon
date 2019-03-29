class donkey:
	def talks(self):
		print("talks like a donkey")
class cat:
	def talks(self):
		print("talks like a cat")
class dog:
	def talks(self):
		print("talks like a dog")
class monkey:
	def talks(self):
		print("talks like a monkey")

def m1(a):
	a.talks()

l=[donkey(),cat(),dog(),monkey()]
for i in l:
	m1(i)


