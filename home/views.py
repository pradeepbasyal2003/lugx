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
        self.views['products']
        return render(request , 'index.html',self.views)


class ProductDetail(Base):

    def get(self , request):
        return render(request , 'product-details.html')