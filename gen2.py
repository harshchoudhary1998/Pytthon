def m1(num):
	n1=1
	while n1<=num:
		yield n1
		n1=n1+1
a=m1(100)
for x in a:
	print(x)
