from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Brand, Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "sku", "name", "price", "id_brand", "queries", "created_at")
        read_only_fields = ("created_at", "queries")


class UserSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "products"]
