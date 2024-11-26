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
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    for item in wishlist_items:
        print(f"Product in wiahlist: {item.product.name}, Price: {item.product.price}, Image URL: {item.product.image.url if item.product.image else 'No Image'}")
    print("wishlist_view items",wishlist_items)
    context = {
        'wishlist_items': wishlist_items
    }
    return render(request, 'products/wishlist.html', context)

@login_required
def add_to_wishlist_view(request,product_id):
    """Add product to wishlist"""
    product=get_object_or_404(Products,pk=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    print(wishlist_item)

    if created:
        messages.success(request, f"{product.name} has been added to your wishlist!")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    
    # Redirect to the wishlist page
    return redirect(reverse('wishlist'))   # Redirect to the wishlist page

@login_required
def remove_from_wishlist_view(request, item_id):
    """Remove product from wishlist using pop method"""
    # Get the wishlist from session
    wishlist_items = request.session.get('wishlist', {})
    print("Wishlist before removal:", wishlist_items)

    # Ensure item_id is treated as a string for consistency (if using SKU as key)
    item_id = str(item_id)
    print("item_id to remove:", item_id)

    print("Available keys in wishlist:", wishlist_items.keys())

    # Remove the item from the wishlist using pop()
    removed_item = wishlist_items.pop(item_id,None)
    print(f"Removed item:" ,removed_item)
    if removed_item:
        request.session['wishlist'] = wishlist_items  # Update the session
        messages.info(request, f'Item removed from your wishlist.')
    else:
        messages.info(request, f'The item is not in your wishlist.')

    # Now we need to remove the product from the database using SKU
    try:
        product = Products.objects.get(sku=item_id)  # Get the product by SKU
        print(f"Product {product.name} removed.")
    except Products.DoesNotExist:
        print("Product with SKU does not exist.")

    # Redirect to the wishlist page after removal
    return redirect(reverse('wishlist'))