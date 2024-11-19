from django.shortcuts import render,redirect,reverse,get_object_or_404,HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CheckoutForm
from .models import Checkout,CheckoutLineItem
from products.models import Products
from django.conf import settings

from shopping_bag.contexts import shopping_bag_contents

import stripe
import json

# Create your views here.

@require_POST
def cache_checkout_data(request):
    print("Entered Cache checkout data")
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        print(pid)
        stripe.api_key=settings.STRIPE_SECRET_KEY
        print(stripe.api_key)
        stripe.PaymentIntent.modify(pid,metadata={
            'bag':json.dumps(request.session.get('bag',{})),#shopping cart info
            'save_info':request.POST.get('save_info'),#weather user needs to save info
            'username':request.user,#username of logged in user
        })
        print("cache_success")
        return HttpResponse(status=200)
    except Exception as e:
        print(f"Error in cache_checkout_data: {e}")
        messages.error(request,'Sorry, your payment cannot be \
                       processed right now.Please try again later ')
        return HttpResponse(content=e,status=400)

def payment_view(request):
    """
    Processing payment
    checks the user's order is valid and all items in the shopping bag are available.
    A Stripe PaymentIntent is created for processing the payment.
    """
    print("Enterd payment view")
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    print(stripe_public_key)
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    print(stripe_secret_key)

    print(f"Request method: {request.method}")
    if request.method == 'POST':
        
        #retrives the shopping bag from user session
        bag=request.session.get('shopping_bag',{})
        print(bag)
        #collects user enters info from post data into dictionary
        form_data = {
            'full_name' : request.POST['full_name'],
            'email' : request.POST['email'],
            'phone_number' : request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode':request.POST['postcode'],
            'country':request.POST['country'],
        }
       
        #creating instance of checkoutform 
        checkout_form = CheckoutForm(form_data)
        print("checkout form:",checkout_form)
        if checkout_form.is_valid():
            print("form is valid")
            order=checkout_form.save(commit=False)#save the form if it is valid
            print(f"order:",order)
            print(f"order created with order_number:{order.order_number}")
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product=Products.objects.get(id=item_id)
                    if isinstance(item_data,int):
                        checkout_line_item = CheckoutLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        checkout_line_item.save()
                        print(f"Saved line item for product ID {item_id} with quantity {item_data}")
                except Products.DoesNotExist:
                    print(f"Product ID {item_id} not found in database")
                    messages.error(request,(
                        "One of the products in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shopping_bag'))
                print("Redirecting to payment_success page") 
                
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_success',args=[order.order_number]))
        else:
            messages.error(request,'There was  an error with your form.'
                           'Please double check your informations.')           
    else:
        bag=request.session.get('shopping_bag',{})
        if not bag:
            print("Shopping bag is empty")
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

def payment_success_view(request,order_number):
    """
    Handling successful payment
    """
    print("Rendering payment success view")
    save_info=request.session.get('save_info')
    order=get_object_or_404(Checkout,order_number=order_number)
    print(f"Order found with order_number: {order_number}")
    messages.success(request, f'Order successfully processed! \
                     Your order number is {order_number}. A confirmation \
                    email will be sent to {order.email}')
    
    if 'bag' in request.session:
        del request.session['bag']

    template='payment/payment_success.html'
    context = {
        'order':order,
    }
    print("Rendering payment_success template")
    return render(request,template,context)