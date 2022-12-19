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
    item = get_object_or_404(Item, pk=item_id)
    lst = item.review_set.order_by('-r_rating')

    if request.method == 'POST' and request.POST.get('form_id') == "LIKE":
        item.item_likes += 1
        item.save()

    elif request.method == 'POST' and request.POST.get('form_id') == "REVIEW":
        item.review_set.create(r_text=request.POST.get('r_text'))
        item.save()

    elif request.method == 'POST' and request.POST.get('form_id').isdigit():
        review = item.review_set.get(r_id=request.POST.get('form_id'))
        review.r_rating += 1
        review.save()
        item.save()

    return render(request, 'shop/detail.html', {'item': item, 'lst': lst})
