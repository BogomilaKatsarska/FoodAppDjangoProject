from django.shortcuts import render, redirect
from food.forms import ItemForm
from food.models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


# def detail(request, item_id):
#     item = Item.objects.get(id=item_id)
#     context = {
#         'item': item,
#     }
#     return render(request, 'food/detail.html', context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', context)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    context = {
        'form': form,
        'item': item,
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', context)


def delete_item(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item,
    }
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', context)