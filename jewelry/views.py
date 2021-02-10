from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):

    prods = Product.objects.all()
    return render(request, 'index.html',{'prods':prods})