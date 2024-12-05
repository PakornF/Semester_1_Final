class BankAccount:
    num_bank_account = 0
    interest_rate = 0.02
    def __init__(self, accountID='', balance=0):
        self.accountID = accountID
        self.balance = balance
        BankAccount.num_bank_account += 1
    def set_account_ID(self, newID):
        self.accountID = newID
    def set_balance(self, new_balance):
        self.balance = new_balance
    def get_account_ID(self):
        return self.accountID
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
    def withdrawal(self, amount):
        self.balance -= amount
    def __str__(self):
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"
    def add_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    @staticmethod
    def get_num_bank_account():
        return BankAccount.num_bank_account

    @staticmethod
    def get_interest_rate():
        return BankAccount.interest_rate

    @staticmethod
    def set_interest_rate(new_rate):
        BankAccount.interest_rate = new_rate

class BankAccountApp:
    account1 = BankAccount('1001', 500)
    account2 = BankAccount('1002', 4000)
    account1.deposit(200)
    account1.add_interest()
    print(account1)
    account2.add_interest()
    print(account2)
    BankAccount.set_interest_rate(0.1)
    print(account1.get_num_bank_account())
    print(account2.get_num_bank_account())
    print(BankAccount.get_num_bank_account())
    print(account1.get_interest_rate())
    print(account2.get_interest_rate())
    print(BankAccount.get_interest_rate())

