
from django.urls import path , include
from .views import *
urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('product-detail' , ProductDetail.as_view() , name='product-detail')
]
