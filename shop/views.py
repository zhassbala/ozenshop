from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Item, Subcategory


def index(request):
    items_list = Item.objects.all()
    categories_list = Subcategory.objects.all()
    return render(request, 'index.html', {'items_list': items_list, 'categories_list': categories_list})


def redirect_to_mainpage(request):
    return HttpResponseRedirect(reverse('shop:mainpage'))


def detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except:
        raise Http404('Товар не найден')
    categories_list = Subcategory.objects.all()

    return render(request, 'detail.html', {'item': item, 'categories_list': categories_list})


def search(request):
    items_list = Item.objects.filter(name__icontains=request.GET['searchword'].capitalize())
    categories_list = Subcategory.objects.all()
    return render(request, 'index.html', {'items_list': items_list, 'categories_list': categories_list})


def category_filter(request, cat):
    items_list = Item.objects.filter(category__subcategory_name=cat)
    categories_list = Subcategory.objects.all()
    return render(request, 'index.html', {'items_list': items_list, 'categories_list': categories_list})
