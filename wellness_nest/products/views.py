from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from.models import Products, Category

# Create your views here.

def all_products(request):
    """ A view to display all products image and details
        and filter the displayed products based on search query"""

    products = Products.objects.all()
    query=None
    categories=None

    if request.GET:
        if 'search_term' in request.GET:
            query = request.GET['search_term']
            if not query:
                messages.error(request,"Please provide a search criteria and try again!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            print(categories)
            products= products.filter(category__name__in=categories)
            print(products)
            categories=Category.objects.filter(name__in=categories)

    context={
        'products' : products,
        'search_term':query,
        'current_categories':categories,
    }

    return render(request,'products/products.html', context)


def product_detail(request,product_id):
    """ A view to display indivudual product details with description"""

    product = get_object_or_404(Products,pk=product_id)

    context={
        'product' : product,
    }

    return render(request,'products/product_detail.html', context)