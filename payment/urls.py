from django.urls import path
from .import views
from .webhooks import webhook


urlpatterns=[
    path('payment_view/',views.payment_view,name='payment'),
    path('payment_success_view/<order_number>/',views.payment_success_view,name='payment_success'),
    path('cache_checkout_data/',views.cache_checkout_data,name='cache_checkout_data'),
    path('webhook/', webhook, name='webhook'),
]
