from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('mens', views.mens, name='mens'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('womens', views.womens, name='womens'),
    path('boys', views.boys, name='boys'),
    path('girls', views.girls, name='girls'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('checkout', views.checkout, name='checkout'),
    path('checkout.html', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
    
]
