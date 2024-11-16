from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.contrib import messages
from .forms import CheckoutForm
from .models import Checkout,CheckoutLineItem
from products.models import Products
from django.conf import settings

from shopping_bag.contexts import shopping_bag_contents

import stripe

# Create your views here.


def payment_view(request):
    """
    checks the user's order is valid and all items in the shopping bag are available.
    A Stripe PaymentIntent is created for processing the payment.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag=request.session.get('shopping_bag',{})

        form_data = {
            'full_name' : request.POST['full_name'],
            'email' : request.POST['email'],
            'phone_number' : request.POST['phone_number'],
            'street_adress1': request.POST['street_address1'],
            'street_adress2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode':request.POST['postcode'],
            'country':request.POST['country'],
        }
        checkout_form = CheckoutForm(form_data)#creating the form data 
        if checkout_form.is_valid():
            order=checkout_form.save()#save the form if it is valid
            for item_id, item_data in shopping_bag.items():
                try:
                    product=Products.objects.get(id=item_id)
                    if isinstance(item_data,int):
                        checkout_line_item = CheckoutLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        checkout_line_item.save()
                except Products.DoesNotExist:
                    messages.error(request,(
                        "One of the products in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_bag'))
                
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success',args=[order.order_number]))
        else:
            messages.error(request,'There was  an error with your form.'
                           'Please double check your informations.')
                
    else:
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

def payment_success(request,order_number):
    """
    Handling successful payment
    """
    save_info=request.session.get('save_info')
    order=get_object_or_404(Checkout,order_number=order_number)
    messages.success(request, f'Order successfully processed! \
                     Your order number is {order_number}. A confirmation email will be sent to {order.email}')
    
    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template='payment/payment_success.html'
    context = {
        'order':order,
    }

    return render(request,template,context)