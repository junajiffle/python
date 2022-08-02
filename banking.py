class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
    
    def withdraw(self, with_amt):
        if self.balance >= with_amt:
            self.balance -= with_amt
            print("Withdrawal Accepted")
        else:
            print("Insufficient funds")
acct = Account('Juna',100)   
acct.deposit(100)
acct.withdraw(90)
acct.withdraw(500)
