import csv
with open("E:\eg.csv","r") as f:
    f=csv.reader(f)
    print(f)
    rows=[]
    for row in f:
        print(row)
      #  rows.append(row)
   # print("no of rows:",rows.line_num)
        
