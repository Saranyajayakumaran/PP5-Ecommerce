from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    """
    The model customizes the display of the Testimonial model
    in the Django admin interface by specifying the fields
    to be shown in the list view. It includes:

    - 'user': The user associated with the testimonial.
    - 'message': The content of the testimonial message.
    - 'created_at': The timestamp when the testimonial was created.

    Attributes:
        list_display (tuple): A tuple of field names that
        should be displayed in the list view of the
        Testimonial model in the admin.
    """
    list_display = (
        'user',
        'message',
        'created_at'
    )


admin.site.register(Testimonial, TestimonialAdmin)
