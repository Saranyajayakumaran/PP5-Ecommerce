from django.urls import path
from .import views

urlpatterns=[
    path('',views.payment_view,name='payment'),
    path('checkout_success/<order_number>',views.payment_success,name='payment_sucess')
]
