from threading import *
def show(slef):
	print("This is show thread")
	for i in range(5):
		print("Run Show Thread",current_thread().getName())
def show2(slef):
	print("This is show thread")
	for i in range(2):
		print("Run Show Thread",current_thread().getName())


a1=pp()
t=Thread(target=a1.show)
t.start()
t=Thread(target-a1.show2)
t.start()
for i in range(10):
	print("Main thread",current_thread().getName())