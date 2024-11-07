from django.shortcuts import render,redirect

# Create your views here.

def shopping_bag_view(request):
    "A view that display the contents of bage"

    return render(request,'shopping_bag/shopping_bag.html')

def add_to_bag_view(request,item_id):
    """Add quantity of selected product to shopping bag"""

    quantity = int(request.POST.get('quantity'))
    redirect_url=request.POST.get('redirect_url')
    shopping_bag = request.session.get('bag',{})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(redirect_url)