from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Item


def index(request):
    latest_list = Item.objects.order_by('-item_date')
    template = loader.get_template('shop/index.html')
    context = {
        'latest_list': latest_list,
    }
    return render(request, 'shop/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=1)
    return render(request, 'shop/detail.html', {'item': item})
