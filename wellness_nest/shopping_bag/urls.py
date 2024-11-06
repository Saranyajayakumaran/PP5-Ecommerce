from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.shopping_bag_view, name='shopping_bag')
]
