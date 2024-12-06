from django.db import models
from django.conf import settings


class Category(models.Model):

    """Model for Categories of the products"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=254,
                            unique=True, null=True,
                            blank=True)  # used for SEO

    def __str__(self):
        return self.name or ""

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Model for all products fields """

    class Meta:
        verbose_name_plural = 'Products'

    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(max_length=50)
    expected_dispatch = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"
