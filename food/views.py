from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from food.models import Item


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)


def item(request):
    return HttpResponse('This is an item view')


def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)