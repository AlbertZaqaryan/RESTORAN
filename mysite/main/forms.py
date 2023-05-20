from django import forms
from .models import Category, Product_Type

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    
class Product_TypeForm(forms.ModelForm):
    class Meta:
        model = Product_Type
        fields = ['category', 'name']