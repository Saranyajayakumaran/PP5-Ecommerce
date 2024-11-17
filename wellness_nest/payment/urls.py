from django.urls import path
from .import views
from .webhooks import webhook


urlpatterns=[
    path('',views.payment_view,name='payment'),
    path('payment_success_view/<order_number>/',views.payment_success_view,name='payment_success'),
    path('wh/',webhook,name='webhook')
]
