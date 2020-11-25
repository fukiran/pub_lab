class Customer():

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def buy_drink(self, drink):
        self.wallet -= drink.price

    def can_afford(self, drink):
        if self.wallet >= drink.price:
            return True