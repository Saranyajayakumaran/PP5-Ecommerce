from django.shortcuts import render, redirect,HttpResponse, reverse, get_object_or_404
from django.contrib import messages


from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from.models import Products, Category, Wishlist
from .forms import ProductForm

# Create your views here.

def all_products_view(request):
    """ A view to display all products image and details
        and filter the displayed products based on search query"""


    products = Products.objects.all()
    query=None
    categories=None
    sort=None
    direction=None

    if request.GET:
        # Sorting logic
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            #print("Sort key received:", sortkey)
            sort = sortkey  
            # Sorting by name - ensure it's case-insensitive
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'category':
                sortkey = 'category__name' 
            
            # Handling the sorting direction (if specified in the query parameters)
            if 'direction' in request.GET:
                direction = request.GET['direction']
                #print("Sort direction received:", direction)
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                    print("Sorting in descending order")
            
            # Apply the sorting to the queryset
            products = products.order_by(sortkey)
            #print("Products after sorting:", products)
        if 'category' in request.GET:
            #print(request.GET)
            categories = request.GET['category'].split(',')
            #print(categories)
            #filters the products queryset to include only requested category
            products= products.filter(category__name__in=categories)
            #print(products)
            #retrieves the Category object for requested category.
            categories=Category.objects.filter(name__in=categories)

        if 'search_term' in request.GET:
            query = request.GET['search_term']
            if not query:
                messages.error(request,"Please provide a search criteria and try again!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting=f'{sort}_{direction}'
    print("Current sorting:", current_sorting)

    context={
        'products' : products,
        'search_term':query,
        'current_categories':categories,
        'current_sorting':current_sorting,
    }

    return render(request,'products/products.html', context)


def product_detail_view(request,product_id):
    """ A view to display indivudual product details with description"""

    product = get_object_or_404(Products,pk=product_id)

    context={
        'product' : product,
    }

    return render(request,'products/product_detail.html', context)


@login_required
def add_product_view(request):
    """Add product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid')
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        'form': form,   
    }

    return render(request, template, context)


@login_required
def edit_product_view(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Products, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product= form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product_view(request,product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Products, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('products'))


@login_required
def wishlist_view(request):
    """Display all the items in wishlist"""
    print("Entet wishlist view")
    wishlist_items = request.session.get('wishlist',{})
    print(wishlist_items)

    wishlist_details = []
    for item_id, details in wishlist_items.items():
        details[item_id]=item_id
        wishlist_details.append(details)
        context = {
            'wishlist_details': wishlist_details,
        }
        print("wishlist_details:",context)
    return render(request,'products/wishlist.html',context)


@login_required
def add_to_wishlist_view(request,item_id):
    """Add product to wishlist"""
    product=get_object_or_404(Products,pk=item_id)
    wishlist_items = request.session.get('wishlist',{}) 
    print(wishlist_items)
    if str(item_id) not in wishlist_items:
        wishlist_items[str(item_id)] = {
            'name': product.name,
            'price' : str(product.price),
            'image' : product.image.url if product.image else None,
            'sku':product.sku
        }
        request.session['wishlist'] = wishlist_items
        messages.info(request, f'{product.name} added to your wishlist')
    else:
        messages.info(request, f'{product.name} is already in your wishlist')
    
    # Redirect to the wishlist page
    return redirect(reverse('wishlist'))   # Redirect to the wishlist page

@login_required
def remove_from_wishlist_view(request, item_id):
    """Remove product from wishlist"""
    wishlist_items = request.session.get('wishlist', {})
    print(f"Wishlist before removal: {wishlist_items}")

    # Check if the item exists in the wishlist
    if str(item_id) in wishlist_items:
        # Remove the item from the wishlist
        del wishlist_items[str(item_id)]
        request.session['wishlist'] = wishlist_items
        product = get_object_or_404(Products, pk=item_id)  # Get product to show the name in the message
        messages.info(request, f'{product.name} has been removed from your wishlist')
    else:
        messages.info(request, "Item not found in your wishlist")
    
    # Redirect to the wishlist page
    return redirect(reverse('wishlist'))