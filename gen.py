def mygen():
	yield "pp"
	yield "hc"
	yield "nn"
print(type(mygen()))
a=mygen()
print(next(mygen()))
print(next(mygen()))
print(next(a))
print(next(a))
print(next(a))

