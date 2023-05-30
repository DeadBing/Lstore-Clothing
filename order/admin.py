from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'price', 'quantity', 'size']
    list_filter = ['id', 'order']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'street', 'house', 'city', 'region', 'index', 'country', 'comment']
    list_filter = ['id', 'first_name']

class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'street', 'house', 'city', 'region', 'index', 'country', 'comment', 'customer']
    list_filter = ['id', 'first_name']
    actions = None

    def save_model(self, request, obj, form, change):
        if not obj.customer:
            obj.customer = request.user
        obj.save()

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)