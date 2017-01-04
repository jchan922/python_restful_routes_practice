from django.shortcuts import render, redirect, HttpResponse
from .models import Product

# Create your views here.
def index(request):

    context = {
        "products": Product.objects.all()
    }

    return render(request, 'products/index.html', context)

def new(request):
    return render(request, 'products/new.html')

def create(request):
    name=request.POST['product_name']
    description=request.POST['product_description']
    price=request.POST['product_price']

    add_product = Product.objects.create(product_name=name, product_description=description, product_price=price)
    print add_product

    return redirect('/products')

def show(request, id):
    product = Product.objects.get(id=id)

    context = {
        "product": product
    }

    return render(request,'products/show.html', context)

def edit(request, id):
    product = Product.objects.get(id=id)

    context = {
        "product": product
    }

    return render(request,'products/edit.html', context)

def update(request, id):
    name=request.POST['product_name']
    description=request.POST['product_description']
    price=request.POST['product_price']

    product_to_update = Product.objects.filter(id=id).update(product_name=name, product_description=description, product_price=price)

    return redirect('/products')

def destroy(request, id):
    product_to_delete = Product.objects.filter(id=id)
    product_to_delete.delete()
    return redirect('/products')
