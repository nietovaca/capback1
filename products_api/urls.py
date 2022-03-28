from django.urls import path
from . import views

urlpatterns = [
    path('api/category', views.CategoryList.as_view(), name='category_list'),
    path('api/products', views.ProductList.as_view(), name='product_list'),
    path('api/category/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('api/products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
]