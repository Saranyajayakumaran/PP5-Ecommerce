from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.shopping_bag_view, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag_view, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag_view, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_item_view, name='remove_item')

]
