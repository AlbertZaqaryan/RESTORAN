from django.shortcuts import render, redirect
from .forms import CategoryForm, Product_TypeForm
from .models import Category, Product_Type
from django.urls import reverse
from django.http import HttpResponse
from django.http import  HttpResponsePermanentRedirect

delete_ = 0

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = CategoryForm()
    category_list = Category.objects.all()
    return render(request, 'main/index.html', context={
        'form':form,
        'category_list':category_list
    })

def index_detail(request, id):
    global delete_
    cat_item = Category.objects.get(pk=id)
    delete_ = cat_item.id
    if request.method == 'POST':
        form = Product_TypeForm(request.POST)
        if form.is_valid():
            Product_Type.objects.create(**form.cleaned_data)
            return redirect(f'http://127.0.0.1:8000/category/{delete_}/')
    else:
        form = Product_TypeForm()
    category_type_list = Category.objects.filter(pk=id)
    return render(request, 'main/index_detail.html', context={
        'form':form,
        'category_type_list':category_type_list,
        'cat_item':cat_item
    })


def delete_prod(request):
    global delete_
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        Product_Type.objects.filter(id=prod_id).delete()
        return redirect(f'http://127.0.0.1:8000/category/{delete_}/')