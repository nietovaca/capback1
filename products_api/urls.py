from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('api/products', views.ProductList.as_view(), name='product_list'),
    path('api/products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)