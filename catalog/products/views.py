from django.contrib.auth.models import User
from rest_framework import generics, serializers

from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


