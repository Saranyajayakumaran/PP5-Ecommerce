from django.urls import path
from .import views


urlpatterns = [
    path('testimonials/', views.testimonials_view, name='testimonials'),
    path('testimonials/add/', views.add_testimonials_view , name='add_testimonials'),
    path('testimonials/delete/<int:testimonial_id>', views.delete_testimonials_view , name='delete_testimonials')

]