from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

def index(request):
    products=Products.objects.all()
    return  render(request,'index.html',{'products':products})


def old(request):
    return  HttpResponse("old items")

