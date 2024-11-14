from django.shortcuts import render,redirect,reverse
from django.contrib import messages

from .form import CheckoutForm

# Create your views here.


def payment_view(request):
    shopping_bag=request.session.get('shopping_bag',{})
    if not shopping_bag:
        messages.error(request, "Your Bag is empty at the moment")
        return redirect(reverse('products'))

    checkout_form = CheckoutForm() 
    template = 'payment/payment.html'
    context={
        'checkout_form' : checkout_form,
    }

    return render(request,template,context)