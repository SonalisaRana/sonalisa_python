#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello", self.cname,"your Account",self.acno,"Is opened with",self.balance,"Rs.")
        
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Deposit of",amount,"Is sucessfull")

    def withdraw(self,amount):
        if amount<=self.balance
             self.balance=self.balance-amount
        else:
            print("Sorry You need Another",amount,self.balance,"RS")
            
    def checkBalance(self):
        print("Current Balance:",self.balance)
b1=Bank()
 
cname=input("Enter Customer Name:")
acno=int(input("Enter Account Number:"))
balance=int(input("Enter Initil Balance:"))
            
b1.openAccount(cname,acno,balance)

while True:
    
    print("*"*50)
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")
    print("*"*50)
    
    choice=int(input("Enter your choice:"))
    print("*"*50)
    
    if choice==1:
        amount=int(input('Enter Deposit Amount'))
        b1.deposit(amount)
        print("*"*50)
        
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount"))
        b1.withdraw(amount)
        
    elif choice==3:
        b1.checkBalance()
        
    else:
        print("Thank You Using Our Service")
        break
        
        
    
    
    


# In[ ]:





# In[ ]:




