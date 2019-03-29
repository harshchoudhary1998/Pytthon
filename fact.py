def fact(num):
	fact1=1
	if num==1 or num==0:
		return 1
	else:
		fact1=num*fact(num-1)
	return fact1

for i in range(1,10):
	print("factorial for",i,"=",fact(i))
             