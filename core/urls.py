from django.urls import path, include
from .views import BoxCheckout, Home, Aboutus, Cart, Business_card, All_products, Business_stationary, Large_format, Marketing_products, Checkout,  Order_placed, get_status, Contactus, BoxCheckout, Emptycart, Search


urlpatterns = [
     path('', Home, name='home'),
     path('all-Products', All_products, name='all_products' ),
     path('aboutus', Aboutus.as_view(), name='aboutus'),
     path('cart', Cart, name='cart'),
     path('checkout', Checkout, name='checkout'),
     path('b-checkout', BoxCheckout, name='b-checkout'),
     path('empty-cart', Emptycart, name='empty-cart'),
     path('search', Search, name='search'),
     # Catogery 
     path('business-cards', Business_card, name='business-cards' ),
     path('business-Stationary', Business_stationary, name='business_stationary'),
     path('marketing-Products', Marketing_products, name='marketing_products'),
     path('large-Format', Large_format, name='large_format'),
#    path('PostCardDetail', PostCardDetail, name='PostCardDetail')
     # Order Id & Status
     path('order',Order_placed, name='order' ),
     path('order-status',get_status, name='order_status'),
     path('contact-us',Contactus, name='contact-us'),

]
