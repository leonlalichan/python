from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from ecomapp.models import Product, Category
from .import models

# Create your views here.



def allProductCat(request,cslug=None):
    cpage=None
    products=None
    if cslug!=None:
        cpage=get_object_or_404(Category,slug=cslug)
        products=Product.objects.all().filter(category=cpage,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,'category.html',{'category':cpage,'products':products})

def proDetail(request,cslug,productslug):
    try:
        product=Product.objects.get(category__slug=cslug,slug=productslug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})