from django.http import HttpResponse
from .models import Checkout, CheckoutLineItem
from products.models import Products

import json
import time
import logging

logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        logger.info(f"Unhandled event received: {event['type']}")
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        logger.info(f"Received event: {event}")
        intent = event.data.object
        pid = intent.id
        shopping_bag = json.loads(intent.metadata.shopping_bag)
        save_info = intent.metadata.save_info
        logger.info(f"Shopping bag: {shopping_bag}")
        logger.info(f"Save info: {save_info}")

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        logger.info(f"Billing details: {billing_details}")
        logger.info(f"Shipping details: {shipping_details}")

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
                    phone_number__iexact = shipping_details.phone,
                    street_address1__iexact = shipping_details.address.line1,
                    street_address2__iexact = shipping_details.address.line2,
                    town_or_city__iexact = shipping_details.address.city,
                    postcode__iexact = shipping_details.address.postal_code,
                    country__iexact = shipping_details.address.country,
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
                logger.info(f"Order already exists: {order.order_number}")
                return HttpResponse(
                    content=f'Webhook received: {event["type"]}| SUCCESS: Verified order already in database',
                    status=200) 
        else:
            order = None  
            try:
                order = Checkout.objects.create(
                    full_name = shipping_details.name,
                    email = shipping_details.email,
                    phone_number = shipping_details.phone,
                    street_address1 = shipping_details.address.line1,
                    street_address2 = shipping_details.address.line2,
                    town_or_city = shipping_details.address.city,
                    postcode = shipping_details.address.postal_code,
                    country = shipping_details.address.country,
                    original_bag = shopping_bag,
                    stripe_pid = pid,
                    )
                shopping_bag = json.loads(shopping_bag) 
                for item_id, item_data in json.loads(shopping_bag).items():
                    product=Products.objects.get(id=item_id)
                    if isinstance(item_data,int):
                        checkout_line_item = CheckoutLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        checkout_line_item.save() 
                        logger.info(f"Order created successfully: {order.order_number}")
            except Exception as e:
                if order:
                    order.delete()
                    logger.error(f"Error processing payment intent: {e}")
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
        logger.info(f"Payment intent failed: {event['type']}")
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)