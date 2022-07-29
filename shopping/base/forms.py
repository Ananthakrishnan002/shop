from cProfile import label
from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:

        model = Product
        fields = "__all__"