from django.http import HttpResponse
from .models import Checkout, CheckoutLineItem
from products.models import Products

import json
import time

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        shopping_bag = intent.metedata.bag
        save_info = intent.metedata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        for field,value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        oder_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Checkout.objects.get(
                    full_name__iexact = shipping_details.name,
                    email__iexact = shipping_details.email,
                    phone_number__iexact = shipping_details.phone_nmber,
                    street_address1__iexact = shipping_details.line1,
                    street_address2__iexact = shipping_details.line2,
                    town_or_city__iexact = shipping_details.city,
                    postcode__iexact = shipping_details.postal_code,
                    country__iexact = shipping_details.country,
                    grand_total=grand_total,
                    original_bag = shopping_bag,
                    stripe_pid = pid,
                )
                order_exists = True
                break
            except Checkout.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]}| SUCCESS: Verified order already in database',
                    status=200) 
        else:
            order = None  
            try:
                order = Checkout.objects.create(
                    full_name = shipping_details.name,
                    email = shipping_details.email,
                    phone_number = shipping_details.phone_nmber,
                    street_address1 = shipping_details.line1,
                    street_address2 = shipping_details.line2,
                    town_or_city = shipping_details.city,
                    postcode = shipping_details.postal_code,
                    country = shipping_details.country,
                    original_bag = shopping_bag,
                    stripe_pid = pid,
                    )
                for item_id, item_data in json.loads(bag).items():
                    product=Products.objects.get(id=item_id)
                    if isinstance(item_data,int):
                        checkout_line_item = CheckoutLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        checkout_line_item.save() 
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)   
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Creates order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)