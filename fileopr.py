#open("lecture3.txt")
'''E:\pythonprograms\codes>fileopr.py
Traceback (most recent call last):
  File "E:\pythonprograms\codes\fileopr.py", line 1, in <module>
    open("lecture3.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'lecture3.txt'
 '''
f=open("E:\pythonprograms\lectures\lecture3.txt")
print(f)
#print(f.read())#in this you read complete file and file handler point to and of the file
print(f.read(3))#this will read three byte from the file but now f point to end of the file we got blank as a output
print(f.seek(0))#it will return back to pointer to starting of the file
print(f.tell()) #will tell the current position of file
print(f.readline())#read line by line mwans one line at a time
print(f.readline())
f.seek(0)
print(f.readlines())#read complete file in form of list
f.close()#ones you close this no operation going to beperformed on that particular file
