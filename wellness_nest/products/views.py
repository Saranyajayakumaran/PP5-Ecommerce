from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from.models import Products, Category

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
            print("Sort key received:", sortkey)
            sort = sortkey
            
            # Sorting by name - ensure it's case-insensitive
            if sortkey == 'name_asc':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                print("Annotated for sorting by name (asc):", products)
            elif sortkey == 'name_desc':
                sortkey = '-lower_name'
                products = products.annotate(lower_name=Lower('name'))
                print("Annotated for sorting by name (desc):", products)
            
            # Sorting by price (ascending and descending)
            elif sortkey == 'price_asc':
                sortkey = 'price'
            elif sortkey == 'price_desc':
                sortkey = '-price'

            # Sorting by rating (ascending and descending)
            elif sortkey == 'rating_asc':
                sortkey = 'rating'
            elif sortkey == 'rating_desc':
                sortkey = '-rating'
            
            # Handling the sorting direction (if specified in the query parameters)
            if 'direction' in request.GET:
                direction = request.GET['direction']
                print("Sort direction received:", direction)
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                    print("Sorting in descending order")
            
            # Apply the sorting to the queryset
            products = products.order_by(sortkey)
            print("Products after sorting:", products)
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