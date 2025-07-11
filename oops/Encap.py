# py Encap.py

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance #this variable became private "__variable"
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
    def getbalance(self):
        return self.__balance

#bank accounts
acc=BankAccount("nikunj",2000)
print("Loading opening balance:" ,acc.getbalance())

acc.deposit(200)  
print("balance after deposit:",acc.getbalance())

acc.withdraw(600)
print("balance after withdraw:",acc.getbalance())

#print(acc.__balance) - this will raise an error
       
