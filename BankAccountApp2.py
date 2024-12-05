class BankAccount:

    def __init__(self, account_id:str = '', balance:float = 0):
        self.balance = balance
        self.account_id = account_id

    def set_account(self, new_id):
        self.account_id = new_id

    def set_balance(self, new_balance):
        self.balance = new_balance

    def get_account_id(self):
        return self.account_id

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('You do not have enough money!')

    def __str__(self):
        return f"ID: {self.account_id}, Balance: {self.balance:.2f}"

class BankAccountApp:
    sam = BankAccount()
    sam.deposit(2000)
    print(sam)
    sam.withdrawal(1500)
    print(sam)
    accountID = input("Enter account ID: ")
    balance = float(input("Enter balance: "))
    pat = BankAccount(accountID, balance)
    pat.deposit(1000)
    pat.deposit(5000)
    pat.withdrawal(500)
    print(pat.account_id)
    print(pat.balance)
