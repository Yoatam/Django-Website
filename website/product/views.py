from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def home(request):
   info = ComapanyInformation.objects.first()
   products = Product.objects.all()
   
   data ={
      
      'info':info,
      'products':products
   }
   return render(request,'home.html',data)

def about(request):
   return render(request,'about.html')

def contact_us(request):
   return render(request,'contact.html')

def product(request):
    info = ComapanyInformation.objects.first()
    products = Product.objects.all()
   
    data ={
      
      'info':info,
      'products':products
   }
    return render(request,'product.html',data)