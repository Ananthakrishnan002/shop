

from django.shortcuts import render,redirect
from django.urls import is_valid_path
from .models import Product
from .forms import ProductForm

# Create your views here.


def listProduct(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'list.html', context)


def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        # Product.objects.create(
        #     name = request.POST.get('name'),
        #     price = request.POST.get('price'),
        #     image = request.POST.get('image'),
        #     size = request.POST.get('size'),
        #     description = request.POST.get('description'),
        # )
        if form.is_valid():
            form.save()
        return redirect('list')
    context = {'form':form}

    return render(request, 'addproduct.html', context)
