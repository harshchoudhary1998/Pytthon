l1=[2,3,4,16,5,9]
print(type(filter))
l2=list(filter(lambda x:x*x,l1))
print(type(l2))
print(l2)
l3=filter(lambda c:c%2==0,l1)
print(l3)
for x in l3:
	print(x)
print(l3[1])