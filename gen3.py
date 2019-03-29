def values(num):
	while num>=0:
		yield num
		#yield pp error pp is not defined
		num=num-1
a=values(10)
print(next(a))
print(next(a))
print("----")
for x in a:
	print(x)