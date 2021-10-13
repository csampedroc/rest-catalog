from catalog.products import views
from django import urls
from django.urls.conf import path

urlpatterns = [ 
    path('products/',views.ProductList.as_view()),
    path('products/<int:pk>/',views.ProductDetail.as_view())
]
