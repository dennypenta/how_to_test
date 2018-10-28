from django.test import TestCase

from app.models import Product


class ProductQueryInStockSetTestCase(TestCase):
    def setUp(self):
        self.data = [
            Product.objects.create(title='Title1', price=10, quantity=1),
            Product.objects.create(title='Title2', price=20, quantity=5),
            Product.objects.create(title='Title3', price=30, quantity=0),
        ]

    def tearDown(self):
        Product.objects.all().delete()

    def test_in_stock(self):
        # when

        # given
        res = Product.objects.in_stock()

        # then
        for product in res:
            self.assertGreaterEqual(product.quantity, 1)
