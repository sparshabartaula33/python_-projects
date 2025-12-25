class Account :
    def __init__(self,bal, acc):
        self.balance = bal
        self.account_no = acc
    
    
    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount ,"was creadited")
        print("total amount is : ",self.getbalance())
    
    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount ,"was devited")
        print("total amount is : ",self.getbalance())
    
    def getbalance(self):
        return self.balance

    

acc1 =  Account(1000,1234)
acc1.debit(10)
acc1.credit(1000)
acc1.getbalance()

