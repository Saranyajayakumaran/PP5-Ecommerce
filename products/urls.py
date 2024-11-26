from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products_view, name='products'),
    path('<int:product_id>/',views.product_detail_view, name='product_detail'),
    path('products/category=<str:categories>/', views.all_products_view, name='products_by_category'),
    path('add/',views.add_product_view, name='add_product'),
    path('edit/<int:product_id>/',views.edit_product_view, name='edit_product'),
    path('delete/<int:product_id>/',views.delete_product_view, name='delete_product'),
    path('wishlist/',views.wishlist_view, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist_view, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist_view, name='remove_from_wishlist'),

]