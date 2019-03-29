import sys
class Customer:
	bankname="ppbank"
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance
	def deposit(self,amount):
		self.balance=self.balance+amount
		print("Balance after deposit :",self.balance)
	def withdraw(self,amount):
		if amount>self.balance:
			print("Insufficient balance :")
			sys.exit()
		else:
			self.balance=self.balance-amount
			print("after withdraw balance is :",self.balance)
print("Welcome to bank application")
name=input("Enter customer name :")
c=Customer(name)
while True:
	print("d-Deposit \nw-Withdraw \ne-Exit")
	option=input("Enter your choice :")
	if option=='d':
		amount=float(input("Enter the amount you deposit :"))
		c.deposit(amount)
	elif option=='w':
		amount=float(input("Enter amount you want to withdraw :"))
		c.withdraw(amount)
	elif option=='e':
		print("Thanks for banking ")
		sys.exit()
	else:
		print("Invalid choice ")