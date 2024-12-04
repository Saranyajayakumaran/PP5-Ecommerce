from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='testimonials')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='testimonials', default=1)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"
