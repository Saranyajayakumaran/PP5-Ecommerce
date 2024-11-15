from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .forms import CheckoutForm

from shopping_bag.contexts import shopping_bag_contents

import stripe

# Create your views here.


def payment_view(request):
    shopping_bag=request.session.get('shopping_bag',{})
    if not shopping_bag:
        messages.error(request, "Your Bag is empty at the moment")
        return redirect(reverse('products'))
    

    current_bag = shopping_bag_contents(request)
    total=current_bag['grand_total']
    stripe_total=round(total * 100)

    checkout_form = CheckoutForm() 
    template = 'payment/payment.html'
    context={
        'checkout_form' : checkout_form,
        'stripe_public_key' : 'pk_test_51Q7v6IDWaRaJpdsNRMvH4E5DToW03grHxgBEHzD9gpAiphyZRTEsPjuUsCHLQDG1rQFlCgJTPxgTyx9Sc2MHUKD000gTbuNn7J',
        'client_secret' : 'test client secret',   
        }

    return render(request,template,context)