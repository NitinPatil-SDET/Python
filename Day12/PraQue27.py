#Create Account class with 2 attributes - Balance & Account Number
#Create Method for debit, credit & printing balance 

class Account:
    def __init__(self, bal, accno):
        self.balance=bal
        self.accno=accno

    #Dedbit
    def debit(self, amount):
        self.balance -= amount
        print("Rs ",amount,"was debited")
    
    #Credit
    def credit(self, amount):
        self.balance += amount
        print("Rs ",amount,"is Credited")
    
    #print balance
    def get_balance(self):
        print("The Balance is: ",self.balance)


acc1 = Account(1000, 123450)
print("The Accout number: ", acc1.accno, " has balance: ", acc1.balance)
acc1.debit(500)
acc1.credit(1000)
acc1.get_balance()