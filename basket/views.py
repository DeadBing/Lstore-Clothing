from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .basket import Basket
from .forms import *


@require_POST
def basket_add(request, did):
    basket = Basket(request)
    product = get_object_or_404(Product, id=did)
    form = AddBasketForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 size=cd['size'],
                 update_quantity=cd['update'],
                 update_size=cd['update'],)
    return redirect('basket_detail')


def basket_remove(request, did):
    basket = Basket(request)
    product = get_object_or_404(Product, id=did)
    basket.remove(product)
    return redirect('basket_detail')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})


