from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .forms import CheckoutForm
from django.conf import settings

from shopping_bag.contexts import shopping_bag_contents

import stripe

# Create your views here.


def payment_view(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    shopping_bag=request.session.get('shopping_bag',{})
    if not shopping_bag:
        messages.error(request, "Your Bag is empty at the moment")
        return redirect(reverse('products'))
    

    current_bag = shopping_bag_contents(request)
    total=current_bag['grand_total']
    stripe_total=round(total * 100)
    stripe.api_key=stripe_secret_key

    
    #Create stripe payment intent

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)
    checkout_form = CheckoutForm() 

    if not stripe_public_key:
        messages.warning(request,'Stripe public key is missing.Did you forget to set it in your environment?')

    #Render the template 
    
    template = 'payment/payment.html'
    context={
        'checkout_form' : checkout_form,
        'stripe_public_key' : stripe_public_key,
        'client_secret' : intent.client_secret,   
        }

    return render(request,template,context)