from django.urls import path

from .views import *

urlpatterns = [
    path('', Main.as_view(), name='home'),
    path('category/<int:cid>', ShowCategory.as_view(), name='category'),
    path('product/<int:did>', ProductDetail.as_view(), name='detail'),
    path('search/', Search.as_view(), name='search'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Registration.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]