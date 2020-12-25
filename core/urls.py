from django.urls import path, include
from .views import Home, Aboutus, Cart, detail_calender

urlpatterns = [
     path('', Home, name='Home'),
     path('allproducts', detail_calender, name='allproducts' ),
     path('aboutus', Aboutus.as_view(), name='Aboutus'),
     path('cart', Cart.as_view(), name='Cart'),
     
]
