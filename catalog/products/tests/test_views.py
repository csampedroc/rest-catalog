import pytest
from catalog.products.models import Brand, Product
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class TestBrandAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_brand_list(self):

        Brand.objects.create(name="Brand Test 1")
        Brand.objects.create(name="Brand Test 2")

        url = reverse("brands-list")

        response = self.client.get(url)

        assert Brand.objects.count() == 2
        assert response.status_code == status.HTTP_200_OK

    def test_brand_create(self):

        input_data = {"name": "Brand Test 1"}

        url = reverse("brands-list")

        response = self.client.post(url, data=input_data)

        assert len(response.json()) != 0
        assert response.status_code == status.HTTP_201_CREATED

    def test_brand_detail(self):

        Brand.objects.create(name="Brand Test 1")

        url = reverse("brands-detail", kwargs={"pk": 1})

        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == "Brand Test 1"

    def test_brand_delete(self):

        Brand.objects.create(name="Brand Test 1")

        url = reverse("brands-detail", kwargs={"pk": 1})

        response = self.client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestProductAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_product_list(self):

        brand = Brand.objects.create(name="Brand Test")
        user = User.objects.create(username="user1", password="user1@com", email="user@gmail.com")
        Product.objects.create(sku="PROD-001", name="Product Test 1", price=20, id_brand=brand, created_by=user)
        Product.objects.create(sku="PROD-002", name="Product Test 2", price=10, id_brand=brand, created_by=user)

        url = reverse("products-list")

        response = self.client.get(url)

        assert Product.objects.count() == 2
        assert response.status_code == status.HTTP_200_OK

    def test_brand_detail(self):

        brand = Brand.objects.create(name="Brand Test")
        user = User.objects.create(username="user1", password="user1@com", email="user@gmail.com")
        Product.objects.create(sku="PROD-001", name="Product Test 1", price=20, id_brand=brand, created_by=user)

        url = reverse("products-detail", kwargs={"pk": 1})

        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == "Product Test 1"
