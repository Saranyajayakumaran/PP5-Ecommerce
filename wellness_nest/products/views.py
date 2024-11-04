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

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            print(sortkey)
            sort=sortkey
            print(sort)
            if sortkey=='name':
                sortkey='lowercase_name'
                print(sortkey)
                products=products.annotate(lowercase_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey=f'-{sortkey}'
            products = products.order_by(sortkey)

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