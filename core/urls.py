from django.urls import path, include
from .views import Home, Aboutus, Cart, Business_card, All_products, Business_stationary, Large_format, Marketing_products, Checkout, BC_Detail

urlpatterns = [
     path('', Home, name='home'),
     path('All-Products', All_products, name='all_products' ),
     path('Aboutus', Aboutus.as_view(), name='aboutus'),
     path('Cart', Cart, name='cart'),
     path('Checkout', Checkout, name='checkout'),
     path('Detail', BC_Detail, name='bc_detail'),

     path('Business-Cards', Business_card, name='business_card' ),
     path('Business-Stationary', Business_stationary, name='business_stationary'),
     path('Marketing-Products', Marketing_products, name='marketing_products'),
     path('Large-Format', Large_format, name='large_format'),
     
]
