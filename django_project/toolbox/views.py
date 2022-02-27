from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'toolbox/dashboard.html')


def products(request):
    return render(request, 'toolbox/products.html')


def customer(request):
    return render(request, 'toolbox/customer.html')