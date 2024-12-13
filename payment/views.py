from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import CheckoutForm
from .models import Checkout, CheckoutLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from shopping_bag.contexts import shopping_bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """Caching checkout user data"""
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid,
                                    metadata={
                                        'bag': json.dumps(
                                            request.session.get(
                                                'shopping_bag', {})),
                                        'save_info': request.POST.get(
                                            'save_info'),
                                        'username': request.user,
                                    })
        return HttpResponse(status=200)
    except Exception as e:

        messages.error(request, 'Sorry, your payment cannot be \
                       processed right now.Please try again later ')
        return HttpResponse(content=e, status=400)


def payment_view(request):
    """
    Processing payment
    checks the user's order is valid and all items
    in the shopping bag are available.
    A Stripe PaymentIntent is created for processing the payment.
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        bag = request.session.get('shopping_bag', {})
        #  collects user enters info from post data into dictionary
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        #  creating instance of checkoutform
        checkout_form = CheckoutForm(form_data)

        if checkout_form.is_valid():
            
            order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        checkout_line_item = CheckoutLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        checkout_line_item.save()
                except Product.DoesNotExist:
                    
                    messages.error(request, (
                        "One of the products in your bag"
                        "wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was  an error with your form.'
                           'Please double check your informations.')
    else:
        bag = request.session.get('shopping_bag', {})
        if not bag:
            
            messages.error(request, "Your Bag is empty at the moment")
            return redirect(reverse('products'))

        current_bag = shopping_bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        #  Create stripe payment intent
        intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                payment_method_types=['card'],
            )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town_or_city': profile.default_town_or_city,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.'
                         'Did you forget to set it in your environment?')

    #  Render the template
    template = 'payment/payment.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }

    return render(request, template, context)


def payment_success_view(request, order_number):
    """
    Handling successful payment
    """
    request.session['IsShoppingBagUpdated'] = False
    save_info = request.session.get('save_info')
    
    order = get_object_or_404(Checkout, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
                     Your order number is {order_number}. A confirmation \
                    email will be sent to {order.email}')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template = 'payment/payment_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
