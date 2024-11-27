from django.contrib import admin
from .models import ContactEnquiry

# Register your models here.
class ContactEnquiryAdmin(admin.ModelAdmin):
    
    list_display = ('full_name',
                    'email',
                    'subject',
                    'created_at')
    
    list_filter = ('created_at',)


admin.site.register(ContactEnquiry,ContactEnquiryAdmin)