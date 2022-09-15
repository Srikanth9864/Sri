class BankAccount:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.04    # class variable
    def __init__(self, name, balance):
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
        interest_amount = self.balance * self.__class__.interest_rate
        self.balance = self.balance + interest_amount
        self.transactions.append(f"****** Interest Credited ***** {interest_amount}")

class SavingsBankAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if amount > 10000:
            raise Exception("Cannot withdraw more than 10K from SB Account")
        super().withdraw(amount)

class SalaryAccount(BankAccount):
    # in python convention, it is to be understood as Constant
    # You can change it.. no enforcement is done by Python
    # but you should not change it
    MAX_DRAFT_AMOUNT = 10000
    def __init__(self, name):
        super().__init__(name, balance=0.00)
        self.total_draft_amount_taken = 0.00
        self.is_first_month_salary = True
    
    def deposit(self, amount):
        if self.is_first_month_salary:
            super().deposit( amount + 1000 )
            self.is_first_month_salary = False
        else:
            super().deposit(amount)
        
    def over_draft(self, amount):
        if self.total_draft_amount_taken + amount <= SalaryAccount.MAX_DRAFT_AMOUNT:
            super().deposit(amount)
            self.total_draft_amount_taken += amount
        else:
            raise Exception(f'Max avaibale draft amount exceeds {SalaryAccount.MAX_DRAFT_AMOUNT}')

class SeniorCitizenAccount(BankAccount):
    # over-riding class variable
    # redefining the class variable
    interest_rate = 0.055    # class variable
    
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if amount > 20000:
            raise Exception("Max withdrwal amount is 20K")
        super().withdraw(amount)

class SukanyaSamrudhiAccount(BankAccount):
    # over-riding class variable
    # redefining the class variable
    interest_rate = 0.095    # class variable

    def deposit(self, amount):
        if amount < 1000:
            raise Exception("Min Dep amount is 1K")
        super().deposit(amount)
    
    # completely overriding withdraw method
    def withdraw(self, amount):
        raise Exception("NO NO")

class PenaltyAccount:
    def __init__(self, penalty_amount):
        self.penalty_amount = penalty_amount
    
    def withdraw(self, amount):
        super().withdraw(amount)
        self.balance -= self.penalty_amount

class PensionAccount(PenaltyAccount, BankAccount):
    def __init__(self, name, balance, penalty_amount):
        PenaltyAccount.__init__(self, penalty_amount)
        BankAccount.__init__(self, name, balance)

p = PensionAccount("steve", 10000, 200)
