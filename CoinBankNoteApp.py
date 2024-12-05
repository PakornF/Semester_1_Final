class Coin:

    def __init__(self, value: int = 1):
        self.value = value

    def __str__(self):
        return f"{self.value} Baht Coin"

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

class BankNote:

    def __init__(self, value: int = 20):
        self.value = value

    def __str__(self):
        return f"{self.value} Baht Banknote"

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

class CoinBankNoteApp:
    denominations = [BankNote(1000), BankNote(500), BankNote(100),
                     BankNote(50), BankNote(20), Coin(10),
                     Coin(5), Coin(2), Coin(1)]

    amount = int(input("Input amount : "))

    for denom in denominations:
        value = denom.get_value()
        num = amount // value
        if num > 0:
            print(f"You get {num} of {denom}")
        amount -= num * value
