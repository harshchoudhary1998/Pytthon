# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:49:45 2019

@author: rj
"""

'''from cx_Oracle import *
con=connect("system/system@localhost")
print(type(con))
if con!=None:
    print("connection establish")
    print(con.version)
else:
    print("connection denied")
con.close()'''









'''from cx_Oracle import *
con=connect("system/system@localhost")
try:
    query="insert into harsh values(404,'harsh',2000,'ajmer')"
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Row is updated")
except DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem",e)
finally:
    if con:
        print("connection closed")
    if cursor:
        print("cursor object deleted")'''
        
        
        
        
        
'''from cx_Oracle import *
con=connect("system/system@localhost")
try:
    query="insert into harsh values(:a,:w,:t,:e)" #their is no relationship b/w parametrize variable name and name in the database table
    v=[(10,'cc',100,'bikaner'),(20,'gb',4500,'jaipur')]
    cursor=con.cursor()
    cursor.executemany(query,v)
    con.commit()
    print("Row is updated")
except DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem",e)
finally:
    if con:
        print("connection closed")
    if cursor:
        print("cursor object deleted")'''
        
        
    
    
'''from cx_Oracle import *
con=connect("system/system@localhost")
try:
    query="insert into harsh values(%d,'%s',%d,'%s')" 
    no=int(input("enter serial no"))
    name=input("enter name")
    sal=int(input("enter salary"))
    city=input("enter city")
    cursor=con.cursor()
    cursor.execute(query %(no,name,sal,city))
    con.commit()
    print("Row is updated")
except DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem",e)
finally:
    if con:
        print("connection closed")
    if cursor:
        print("cursor object deleted")   '''   
        
        

        
'''from cx_Oracle import *
con=connect("system/system@localhost")
try:
    query="select * from harsh"  
    curosr=con.cursor()
    cursor.execute(query)
    record=cursor.fetchone()
    print("--------") 
    while record is not None:
        print(record)
        record=cursor.fetchone()

    
except DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem",e)
finally:
    if con:
        print("connection closed")
    if cursor:
        print("cursor object deleted") '''     
        
        
from cx_Oracle import *
con=connect("system/system@localhost")
try:
    query="select * from harsh"  
    cursor=con.cursor()
    cursor.execute(query)
    n=int(input("enter no of records fetch"))
    record=cursor.fetchmany(n)
    print("--------") 
    for row in record:
        print(row[0],end='')
        print(row[1],end='')
        print(row[2],end='')

    

    
except DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem",e)
finally:
    if con:
        print("connection closed")
    if cursor:
        print("cursor object deleted")      
        
        

        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        