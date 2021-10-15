from django.contrib.auth.models import User
from django.test import TestCase

from .models import Brand, Product


class TestBrandModel(TestCase):
    def setUp(self):
        Brand.objects.create(name="Brand Test")

    def test_brand_create(self):
        brand_result = Brand.objects.last()
        assert str(brand_result) == "Brand Test"


class TestProductModel(TestCase):
    def setUp(self):
        brand = Brand.objects.create(name="Brand Test")
        user = User.objects.create(username="user1", password="user1@com", email="user@gmail.com")
        Product.objects.create(sku="PROD-001", name="Product Test 1", price=20, id_brand=brand, created_by=user)

    def test_product_create(self):
        product_result = Product.objects.last()
        assert str(product_result) == "PROD-001 Product Test 1"
