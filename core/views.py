from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Product
# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products':products
    }
    return render(request,'index.html',context)


def blog(request):
    return render(request,'index.html')


def single_blog(request):
    return render(request,'single-blog.html')


def checkout(request):
    return render(request,'checkout.html')


def confirmation(request):
    return render(request,'confirmation.html')


def contact(request):
    return render(request,'contact.html')


def elements(request):
    return render(request,'elements.html')


def tracking(request):
    return render(request,'tracking.html')


