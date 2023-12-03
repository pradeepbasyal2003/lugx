
from django.urls import path , include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('product-detail' , ProductDetail.as_view() , name='product-detail'),
    path('shop' , OurShop.as_view() , name='shop'),
    path('signin' , SignIn.as_view() , name='signin'),
    path('contact' , Contact.as_view() , name='contact'),
]


