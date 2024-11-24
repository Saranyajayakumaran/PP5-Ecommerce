from django.contrib import admin
from .models import Products,Category,Wishlist

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

class WishlistAdmin(admin.ModelAdmin):
    """Display the fields of wishlist in admin"""
    list_display=(
        'user',
        'product',
        "added_on"
    )    

    ordering = ('product',)




admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)

