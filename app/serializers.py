from rest_framework import serializers

from app.models import Product
from app.validators import IsTItleValidator


class ProductCustomerSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[IsTItleValidator()])

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'quantity')
