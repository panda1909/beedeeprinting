from django.urls import path, include
from .views import Home, Aboutus, Cart

urlpatterns = [
     path('', Home.as_view(), name='Home'),
     path('aboutus', Aboutus.as_view(), name='Aboutus'),
     path('cart', Cart.as_view(), name='Cart'),
     
]
