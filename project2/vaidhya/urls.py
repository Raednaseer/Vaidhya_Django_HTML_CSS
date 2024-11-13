from os import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('calculator/',views.calculator,name='calculator'),
    path('contact/',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('products/',views.products,name='products'),
    path('consult/',views.consult,name='consult'),
    path('login/',views.login,name='login'),
    path('consult/success',views.consult_success,name='consult_success'),
    path('signup/',views.signup,name='signup')
]