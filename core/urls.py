from django.urls import path, include
from .views import Home, Aboutus, Cart, business_card

urlpatterns = [
     path('', Home, name='Home'),
     path('Business-Cards', business_card, name='business_card' ),
     path('aboutus', Aboutus.as_view(), name='Aboutus'),
     path('cart', Cart.as_view(), name='Cart'),
     
]
