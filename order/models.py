from django.db import models
from store.models import *


class Order(models.Model):
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    index = models.CharField(max_length=12)
    country = models.CharField(max_length=20)
    comment = models.TextField(max_length=200, null=True)
    updated = models.DateTimeField(auto_now=True)


    def __int__(self):
        return self.pk

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT, verbose_name='Отношение к заказу')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT, verbose_name='Что заказано')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    size = models.CharField(max_length=3, verbose_name='Размер', default='XS')


    def __int__(self):
        return self.pk

    def get_cost(self):
        return self.price * self.quantity