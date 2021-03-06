from catalog.helpers.products import send_data_update_notification
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import generics, permissions

from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer, UserSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()
        product.queries = product.queries + 1
        product.save(update_fields=("queries",))
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        send_data_update_notification(product.sku, product.name)
        return super().update(request, *args, **kwargs)


class BrandList(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
