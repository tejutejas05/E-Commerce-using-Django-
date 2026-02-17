from django.shortcuts import render,get_object_or_404,redirect
from .models import Product

# Create your views here.

def product_list(request):
    product = Product.objects.all()
    return render(request,'store/product_list.html',{'product':product})

def product_details(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'store/product_details.html',{'product':product})


