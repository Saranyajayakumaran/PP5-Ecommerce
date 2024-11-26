from django.contrib import admin
from .models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user',       
        'message',
        'created_at'  
    )
admin.site.register(Testimonial, TestimonialAdmin)