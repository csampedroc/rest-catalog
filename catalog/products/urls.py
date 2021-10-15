from catalog.products import views
from django import urls
from django.urls.conf import path

urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("products/<int:pk>/", views.ProductDetail.as_view()),
    path("brands/", views.BrandList.as_view(), name="brands-list"),
    path("brands/<int:pk>/", views.BrandDetail.as_view(), name="brands-detail"),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]
