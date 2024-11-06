from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products_view, name='products'),
    path('products/<product_id>/',views.product_detail_view, name='product_detail'),
    #path('products/category=<str:categories>/', views.all_products_view, name='products_by_category'),
]