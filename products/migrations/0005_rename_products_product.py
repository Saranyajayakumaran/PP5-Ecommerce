# Generated by Django 4.2 on 2024-12-04 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_testimonial_product'),
        ('payment', '0002_checkout_user_profile'),
        ('products', '0004_wishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]