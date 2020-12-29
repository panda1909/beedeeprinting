from django.urls import path, include
from .views import Home, Aboutus, Cart, Business_card, All_products, Business_stationary, Large_format, Marketing_products, Checkout

urlpatterns = [
     path('', Home, name='Home'),
     path('All-Products', All_products, name='all_products' ),
     path('aboutus', Aboutus.as_view(), name='Aboutus'),
     path('cart', Cart, name='Cart'),
     path('Checkout', Checkout, name='Checkout'),
     

     path('Business-Cards', Business_card, name='business_card' ),
     path('Business-Stationary', Business_stationary, name='Business_stationary'),
     path('Marketing-Products', Marketing_products, name='Marketing_products'),
     path('Large-Format', Large_format, name='Large_format'),
     
]
