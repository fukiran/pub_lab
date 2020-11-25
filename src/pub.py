

class Pub():
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

        
    def sell_drink(self, drink, customer):
        if self.check_customer_age(customer) == True:
            self.till += drink.price

    def check_customer_age(self,customer):
        if customer.age >= 18:
            return True