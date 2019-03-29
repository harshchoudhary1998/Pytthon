from faker import Faker
fake=Faker()
print("******")
count=0
for i in range(100):
	count=count+1
	print(count,fake.name(),end="\t")
	print(fake.city(),end="\t")
	#print(fake.email())