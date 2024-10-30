from django.contrib import admin
from .models import Products,Category

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
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
    list_dispaly=(
        'name',
        'friendly_name',
        'slug'
    )

    ordering=('name',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)