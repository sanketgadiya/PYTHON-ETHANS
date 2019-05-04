class bank:
	bank_name = "JAI MATA DI BANK"

	def __init__(self,name,age):
		self.customer = name
		self.umar = age
		self.balance = 0
	
	def get_balance(self):
		return self.balance

	def deposit(self,amount):
		self.balance = self.balance + amount

	def withdraw(self,amount):
		if self.balance >=amount:
			self.balance = self.balance - amount
		else:
			return "[ERROR] Rakkam kami aahe"

cust1 = bank('Amit',40)
cust2 = bank('Harshad',28)
cust3 = bank('Pranav',16)

print "Balance in %s account is %s" %(cust1.customer,cust1.balance)
cust1.deposit(100)
print "Balance in %s account is %s" %(cust1.customer,cust1.balance)
cust1.withdraw(50)
print "Balance in %s account is %s" %(cust1.customer,cust1.balance)


print "Balance in %s account is %s" %(cust2.customer,cust2.balance)
cust2.deposit(1000)
print "Balance in %s account is %s" %(cust2.customer,cust2.balance)
print cust2.withdraw(50000000)
print "Balance in %s account is %s" %(cust2.customer,cust2.balance)




