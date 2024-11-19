from django.urls import path
from . import views

urlpatters = [
    path('',views.profile_view,name='profile')
]