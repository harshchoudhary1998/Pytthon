import time
import gc
class dest:
	def __init__(self):
		print("constructor")
	def __del__(self):
		print("destructor")
a1=dest()
list=[dest(),dest(),dest()]
del list
a1=None
time.sleep(3)
print("End of application")