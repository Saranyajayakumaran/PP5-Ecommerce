from django.shortcuts import render,redirect,reverse,HttpResponse,get_object_or_404
from products.models import Products
from django.contrib import messages

# Create your views here.

def shopping_bag_view(request):
    "A view that display the contents of bage"

    return render(request,'shopping_bag/shopping_bag.html')

def add_to_bag_view(request,item_id):#item_id=Product_id
    """Add quantity of selected product to shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url=request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag',{})#checks weather the user iniate adding item or bag id empty
    print(shopping_bag)
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)


def adjust_bag_view(request,item_id):#item_id=Product_id
    """adjust the quantity of specific product"""

    product=get_object_or_404(Products,pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag',{})#checks weather the user iniate adding item or bag id empty
   
    if quantity > 99:
        messages.error(
            request, 'Quantity must be less than or equal to 99.')
    elif quantity > 0:
        shopping_bag[item_id]=quantity
        messages.success(
            request, f'{product.name} quantity is added to {shopping_bag[item_id]}'
        )
    else:
        shopping_bag.pop(item_id)
        messages.success(request,f'Removed {product.name} from your shopping bag')
        

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(reverse('shopping_bag'))