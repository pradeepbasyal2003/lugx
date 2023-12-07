import random

from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic import View
# Create your views here.

class Base(View):
    views = {}
class HomeView(Base):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        trending_products = Product.objects.filter(labels = "trending").all()
        self.views['trending'] = random.sample(list(trending_products),4)
        mostplayed_products = Product.objects.filter(labels = "most played").all()
        self.views["most_played"] = random.sample(list(mostplayed_products),6)
        featured = Product.objects.filter(labels = "featured").all()
        self.views['featured'] =random.sample(list(featured) , 1)


        return render(request , 'index.html',self.views)


class ProductDetail(Base):

    def get(self , request):
        return render(request , 'product-details.html')


class OurShop(Base):


    def get(self,request):
        return render(request , 'shop.html')


class Contact(Base):

    def get(self,request):
        return render(request , 'contact.html')


class SignIn(Base):

    def get(self,request):
        return render(request , 'signin.html')