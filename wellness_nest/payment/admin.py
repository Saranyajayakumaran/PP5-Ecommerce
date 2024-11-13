from django.contrib import admin
from .models import Checkout, CheckoutLineItem

# Register your models here.

class CheckoutLineItemAdmininline(admin.TabularInline):
    """ Check out line item fileds in admin"""
    model = CheckoutLineItem
    readonly_fields = ('lineitem_total',)


class CheckoutAdmin(admin.ModelAdmin):
    
    """Display the fields in admin"""

    inlines = (CheckoutLineItemAdmininline,)

    readonly_fields = ('order_number','date',
                        'delivery_cost',
                        'order_total',
                        'grand_total')
    
    fields=(
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'delivery_cost',
        'order_total',
        'grand_total'
    )

    list_display=('order_number', 
                  'date',
                  'full_name',
                  'delivery_cost',
                  'order_total',
                  'grand_total')

    ordering = ('-date',)

admin.site.register(Checkout,CheckoutAdmin)