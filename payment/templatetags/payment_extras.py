from django import template


register = template.Library()


@register.filter
def calc_subtotal(price, quantity):
    """Calculate the subtotal by multiplying price and quantity."""
    return price * quantity
