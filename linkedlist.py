# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:04:45 2019

@author: rj
"""

class ListNode:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        #create a single Node
    def __repr__(self):      
        return repr(self.data) #repr(object)
#return printable statement of the object
#if you use __str__ then we get different output which was readable to human but not python interpreter
#A class can control what this function returns for its instances by defining a __repr__() method.
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def show(self):
        nodes=[]
        curr=self.head
        while curr:
            nodes.append(repr(curr))
            curr=curr.next
        #print(nodes) bath ek he but representation ka fark he
        return '['+','.join(nodes)+']'
        
    
    def prepend(self,data):
        self.head=ListNode(data=data,next=self.head)
        #means ek object bana jiske pointer me ferst node la address he or uss node ko header bana de
        #isme kouch ointer jaise nahi hota bass samajne ke liye likha sab object he
        #insert at begining of the list
        
    def addlast(self,data):
        if not self.head:
            self.head=ListNode(data=data) #simply create new object of that class and root object can have link with child objext
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=ListNode(data=data)
        #insert at the last of linked last
        
    def addinbw(self,middle_node,data):
        if middle_node is None:
            print("mention node is not there")
            return
        curr=self.head
        while curr and curr.data !=middle_node:
            curr=curr.next
            
        NewNode=ListNode(data=data)
        NewNode.next=curr.next
        curr.next=NewNode
        #insert element in between
        
    def find(self,key):
        curr=self.head
        while curr and curr.data!=key:
            curr=curr.next
        return curr #return none if value is not find
    #it simply find the key valye in the list
    
    def remove(self,key):
        curr=self.head
        prev=None
        while curr and curr.data!=key:
            prev=curr
            curr=curr.next
        if prev is None:
            self.head=curr.next
        elif curr:
            prev.next=curr.next
            curr.next=None
        
    def reverse(self):
        curr=self.head
        prev=None
        nex=None
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        self.head=prev
    
    def countNode(self):
        if self.head==None:
            return 0
        else:
            curr=self.head
            count=0
            while (curr!=None):
                curr=curr.next
                count+=1
            return count
        
        
        
        
a=LinkedList()  

a.addlast(10) 
a.addlast(20) 
a.addlast(30) 
a.addlast(40) 
a.addinbw(40,50) 
a.prepend(5)
print(a.countNode())
print(a.show())  
a.reverse()
print(a.show())  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
    

        
    
        