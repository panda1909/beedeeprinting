from django.urls import path, include
from .views import Pillow_Boxes

app_name='boxes'

urlpatterns = [
    path('pillow-boxes-detail', Pillow_Boxes, name='pillow-boxes-detail'),
]