from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework import status

from app.models import Product

from unittest import mock


class ProductViewSetListTestCase(SimpleTestCase):
    data = [
        Product(id=1, title='Title1', price=10, quantity=1),
        Product(id=2, title='Title2', price=20, quantity=5),
    ]
    url = reverse('product-list')

    @mock.patch('app.views.ProductViewSet.queryset', data)
    def test_list(self):
        res = self.client.get(self.url)

        self.assertTrue(status.is_success(res.status_code))
