from django.contrib import admin
from .models import Products,Category

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    
    """Display the fields in admin"""

    list_display=(
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'size'
    )

    ordering = ('sku','name')

class CategoryAdmin(admin.ModelAdmin):

    """Display the fileds of categories in admin"""

    list_display=(
        'name',
        'friendly_name',
        'slug'
    )

    ordering=('name',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
