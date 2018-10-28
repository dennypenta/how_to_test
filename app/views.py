from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from app.models import Product
from app.serializers import ProductCustomerSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.in_stock()
    serializer_class = ProductCustomerSerializer
