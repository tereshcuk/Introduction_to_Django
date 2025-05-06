from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')    
    if sort == 'max_price':
        sort = '-price'        
    elif sort == 'min_price':
        sort = 'price'
        
    phone_objects = Phone.objects.all().order_by(sort)              
    
    
    context = {'phones': phone_objects,}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug= slug)     
    context = {'phone': phone_object}
    return render(request, template, context)
