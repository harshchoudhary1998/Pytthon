l1=[1,2,5,8,3]
print(type(map))
l2=list(map(lambda x:x*x*x,l1))
print(l2)
l1=[1,2,3,4,5,6]
l2=list(filter(lambda x:x*x,l1))
print(l2)

l1=[1,2,3,4]
l2=[7,8,9,10,5]
l3=list(map(lambda a,b:a*b,l1,l2))
print(l3)