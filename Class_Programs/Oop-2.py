class BankAccount:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.05    # class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"**** Inital deposit : {balance} ***********")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount deposited: {amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance = self.balance - amount
        self.transactions.append(f"Amount withdrawn: {amount}")
    
    def statement(self):
        for item in self.transactions:
            print(item)
        print(f"*********** Total Balance {self.balance} ************* ")
    
    def transfer_funds(self, to_account, amount):
        if amount > self.balance:
            raise Exception("Insufficent Funds!!!")
        to_account.deposit(amount)
        self.balance -= amount
    
    def roi(self):
        interest_amount = self.balance * BankAccount.interest_rate
        self.balance = self.balance + interest_amount

c1 = BankAccount("steve", 1000)
c2 = BankAccount("bill", 2000)
c3 = BankAccount("Amy", 3000)
c4 = BankAccount("Alex")