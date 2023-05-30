from django.shortcuts import render, redirect
from .models import OrderItem
from basket.basket import Basket
from .forms import *


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            for item in basket:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         size=item['size'],
                                         price=item['price'],
                                         quantity=item['quantity'],)
            basket.clear()
            return render(request, 'order/created.html',
                          {'order': order})
    else:
        form = OrderForm
    return render(request, 'order/detail.html',
                  {'basket': basket, 'form': form})