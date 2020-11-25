import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Sandy", 10.00, 30, 1)
        self.drink = Drink("Tennants", 2.00, 2)

    def test_customer_has_name(self):
        self.assertEqual("Sandy", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.customer.wallet)

    def test_can_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(8, self.customer.wallet)

    def test_can_customer_afford_drink(self):
        self.assertEqual(self.customer.can_afford(self.drink), True)

    def test_does_customer_get_drunk(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(2, self.customer.drunkenness)


          
