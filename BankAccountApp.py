class BankAccount:

    def __init__(self, account_ID:str = '', balance:int = 0):
        self.balance = balance
        self.account_ID = account_ID

    def set_account(self, newID):
        self.account_ID = newID

    def set_balance(self, newBalance):
        self.balance = newBalance

    def get_account_ID(self):
        return self.account_ID

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
        return f"ID: {self.account_ID}, Balance: {self.balance:.2f}"

class BankAccountApp:
    account = BankAccount("1001", 500)

    while True:
        choice = int(input("Deposit (1), Withdrawal (2), Update (3), or Exit (0): "))
        if choice == 0:
            break
        elif choice == 1:
            amount = float(input("Enter your deposit amount: "))
            account.deposit(amount)
            print(account)
        elif choice == 2:
            amount = float(input("Enter your withdrawal amount: "))
            account.withdrawal(amount)
            print(account)
        else:
            amount = float(input("Enter your update amount: "))
            account.set_balance(amount)
            print(account)

