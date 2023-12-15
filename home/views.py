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
        self.views['featured'] = random.sample(list(featured), 1)


        return render(request , 'index.html',self.views)


class ProductDetail(Base):

    def get(self , request , slug):

        self.views["product"] = Product.objects.get(slug = slug)
        product = Product.objects.get(slug = slug)
        related_product = Product.objects.filter(labels = product.labels )
        self.views["related"] = random.sample(list(related_product),5)
        return render(request , 'product-details.html' , self.views)


class OurShop(Base):
    def get(self,request):
        self.views["products_view"] = Product.objects.all()
        return render(request , 'shop.html' , self.views)

class CategoryView(Base):


    def get(self,request,slug):
        cat_id = Category.objects.get(slug = slug).id
        cat = Category.objects.get(id = cat_id)
        self.views["current_cat"] = cat
        self.views["product_view"] = Product.objects.filter(category = cat)
        self.views["cat"] = Category.objects.all()
        return render(request , 'category.html' , self.views)


class Contact(Base):

    def get(self,request):
        return render(request , 'contact.html')


class SignIn(Base):

    def get(self,request):
        return render(request , 'signin.html')