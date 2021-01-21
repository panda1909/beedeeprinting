from django.urls import path, include
from .views import Home, Aboutus, Cart, Business_card, All_products, Business_stationary, Large_format, Marketing_products, Checkout, BC_Detail, Order_placed, get_status

urlpatterns = [
     path('', Home, name='home'),
     path('all-Products', All_products, name='all_products' ),
     path('aboutus', Aboutus.as_view(), name='aboutus'),
     path('cart', Cart, name='cart'),
     path('checkout', Checkout, name='checkout'),
     path('detail', BC_Detail, name='bc_detail'),
     path('business-Cards', Business_card, name='business_card' ),
     path('business-Stationary', Business_stationary, name='business_stationary'),
     path('marketing-Products', Marketing_products, name='marketing_products'),
     path('large-Format', Large_format, name='large_format'),
#    path('PostCardDetail', PostCardDetail, name='PostCardDetail')
     path('order',Order_placed, name='order' ),
     path('order-status',get_status, name='order_status'),

]
