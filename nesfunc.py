def add(a,b):
	c=a+b
	return c
def nesfun(function,a1,b1):
	res=function(a1,b1)                 ##agar ek bhi return hataya to anarth ho jayega
	return res
d=nesfun(add,3,4)
print(d)