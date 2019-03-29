def m1(*n):
	print(type(n))
	total=0
	for n1 in n:
		total=total+n1
	return total
print(m1())
print(m1(10,20))
print(m1(10,20,30))