from rest_framework import serializers
from products.models import Product


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=12)
    age = serializers.IntegerField()


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
