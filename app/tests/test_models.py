import unittest

from app.models import Product


class ProductInStockTestCase(unittest.TestCase):

    def test_in_stock_true(self):
        for product in [
            Product(quantity=1),
            Product(quantity=5),
        ]:
            self.assertTrue(product.in_stock)

    def test_in_stock_false(self):
        for product in [
            Product(quantity=0),
        ]:
            self.assertFalse(product.in_stock)
