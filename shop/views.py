from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse


def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nslides= n//4 + ceil((n/4)-(n//4))
    # allprods = [[products, range(1, nslides), nslides],
    #             [products, range(1, nslides), nslides]]
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
    # params = {'no_of_slide':nslides,'range':range(1,nslides),'product':products}
    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def productview(request, myid):
    # product fatch by Id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html',{'product' : product[0]})


def search(request):
    return render(request, 'shop/search.html')


def checkout(request):
    return render(request, 'shop/checkout.html')
