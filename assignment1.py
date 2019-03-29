n=int(input("enter the number"));
ty={}
for i in range(1,n+1):
	ty.update({i:i*i})

print(ty)