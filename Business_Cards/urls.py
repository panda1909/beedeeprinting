from django.urls import path, include
from .views import Edge_painted_Detail, BC_Detail, Foil_business_card, Raised_spot_uv, Pantone_business_cards, Plastic_business_card, raised_ink_business_cards

app_name='Business_Cards'

urlpatterns = [
    path('edge-painted-detail', Edge_painted_Detail, name='edge-painted-detail'),
    path('business-card-detail', BC_Detail, name='business-card-detail'),
    path('foil-business-card-detail', Foil_business_card , name='foil-business-card-detail'),
    path('raised-spot-uv-business-card-detail', Raised_spot_uv , name='raised-spot-uv-business-card-detail'),
    path('pantone-business-cards-detail', Pantone_business_cards, name='pantone-business-cards-detail'),
    path('plastic-business-cards-detail', Plastic_business_card, name='plastic-business-cards-detail'),
    path('raised-ink-business-cards-detail', raised_ink_business_cards, name='raised-ink-business-cards-detail'),

]
