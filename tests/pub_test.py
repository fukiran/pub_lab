import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Sandy", 10.00)
        self.drink = Drink("Tennants", 2.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_takes_money(self):
        self.pub.sell_drink(self.drink)
        self.assertEqual(102.00, self.pub.till)

    