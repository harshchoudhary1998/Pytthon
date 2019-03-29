def merge(lisa,lisb):
	a=sorted(lisa)
	b=sorted(lisb)
	c=[]
	indexa=indexb=indexc=0
	tolen=len(a)+len(b)
	while len(c)<tolen and indexa<len(a) and indexb<len(a):
		if a[indexa]<b[indexb]:
			c.append(a[indexa])
			indexa +=1
		else :
			c.append(b[indexb])
			indexb +=1
	if indexa<len(a):
		c.append(a[indexa])
		indexa +=1
	if indexb<len(b):
		c.append(b[indexb])
		indexb +=1
	return c
a=[4,25,8,1]
b=[89,0,23,6,9,1]
c=merge(a,b)
print(c)
    