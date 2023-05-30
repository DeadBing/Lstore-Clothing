from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import ListView, CreateView
from .models import *
from .utils import *
from .forms import *
from basket.forms import *
from order.models import *


class Main(CategoryMixin, ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_mixin = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.all()


class ShowCategory(CategoryMixin, ListView):
    model = Product
    template_name = 'store/products.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category_mixin = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['cid'])


class ProductDetail(CategoryMixin, ListView):
    model = Product
    template_name = 'store/single-product.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddBasketForm()
        category_mixin = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(category_mixin.items()))
        return context

    def get_queryset(self):
        return Product.objects.get(id=self.kwargs['did'])


class Search(ListView):
    template_name = 'store/search.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        return Product.objects.filter(name__iregex=self.request.GET.get('q'))


class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    return redirect('home')

class Registration(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return context

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def profile(request):
    user_orders = Order.objects.filter(customer=request.user)
    user_order_item = OrderItem.objects.all()

    data = {
        'user_orders': user_orders,
        'user_order_item': user_order_item,
    }
    return render(request, 'store/profile.html', data)