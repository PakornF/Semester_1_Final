class Phone:
    def __init__(self, brand:str='Sam', price:int=1000):
        self.brand = brand
        self.price = price

class Samsung(Phone):
    def __init__(self, phone: Phone):
        super().__init__(phone.brand, phone.price)

class Iphone(Phone):
    def __init__(self, brand, price):
        super().__init__(brand, price)
