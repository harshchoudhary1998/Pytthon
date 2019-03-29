def fibb(num):
	a,b=0,1
	while num>=0:
		yield a
		a,b=b,a+b
		num=num-1

num=eval(input("enter the number"))
