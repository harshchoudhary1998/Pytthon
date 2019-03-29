name=["hc","pp","bps"]
clss=["csa","csb","csc"]
c=[[t,c] for t in name for c in clss]
print(c)
'''E:\pythonprograms\codes>listcompre.py
[('hc', 'csa'), ('hc', 'csb'), ('hc', 'csc'), ('pp', 'csa'), ('pp', 'csb'), ('pp', 'csc'), ('bps', 'csa'), ('bps', 'csb'), ('bps', 'csc')]

E:\pythonprograms\codes>listcompre.py
[{'hc', 'csa'}, {'hc', 'csb'}, {'hc', 'csc'}, {'pp', 'csa'}, {'pp', 'csb'}, {'pp', 'csc'}, {'csa', 'bps'}, {'csb', 'bps'}, {'csc', 'bps'}]

E:\pythonprograms\codes>listcompre.py
[['hc', 'csa'], ['hc', 'csb'], ['hc', 'csc'], ['pp', 'csa'], ['pp', 'csb'], ['pp', 'csc'], ['bps', 'csa'], ['bps', 'csb'], ['bps', 'csc']]'''
f=[1,2,3,4,5,6,7,8]
d=[x for x in f if x>5]
print(d)