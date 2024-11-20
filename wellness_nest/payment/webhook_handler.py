from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


from .models import Checkout, CheckoutLineItem
from products.models import Products
from profiles.models import UserProfile

import json
import time
import logging

logger = logging.getLogger(__name__)

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a order confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'payment/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'payment/confirmation_emails/confirmation_email_body.txt',
            {'order':order, 'contact_email':settings.DEFAULT_FROM_EMAIL})
        send_mail (
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL
            [cust_email]
        )

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
        shopping_bag = intent.metadata.shopping_bag
        save_info = intent.metadata.save_info
       

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        #clean data in shipping details
        for field,value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        
        #Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
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
            self._send_confirmation_email(order)   
            return HttpResponse(
                content=f'Webhook received: {event["type"]}| SUCCESS: Verified order already in database',
                status=200) 
        else:
            order = None  
            try:
                order = Checkout.objects.create(
                    full_name = shipping_details.name,
                    user_profile = profile,
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order) 
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