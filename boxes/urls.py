from django.urls import path, include
from .views import Pillow_Boxes, Gable_Boxes, Windows_Boxes, Mailer_Boxes, Kraft_Boxes, Cosmetics_Boxes, Display_Boxes, Sleeve_Boxes, Beverages_Boxes, Candle_Boxes, Autoparts_Boxes, Pizza_Boxes

app_name='boxes'

urlpatterns = [
    path('pillow-boxes-detail', Pillow_Boxes, name='pillow-boxes-detail'),
    path('gable-boxes-detail', Pillow_Boxes, name='gable-boxes-detail'),
    path('window-boxes-detail', Pillow_Boxes, name='window-boxes-detail'),
    path('mailer-boxes-detail', Pillow_Boxes, name='mailer-boxes-detail'),
    path('kraft-boxes-detail', Pillow_Boxes, name='kraft-boxes-detail'),
    path('cosmetics-boxes-detail', Pillow_Boxes, name='cosmetics-boxes-detail'),
    path('display-boxes-detail', Pillow_Boxes, name='display-boxes-detail'),
    path('sleeve-boxes-detail', Pillow_Boxes, name='sleeve-boxes-detail'),
    path('beverage-boxes-detail', Pillow_Boxes, name='beverage-boxes-detail'),
    path('candle-boxes-detail', Pillow_Boxes, name='candle-boxes-detail'),
    path('auto-parts-boxes-detail', Pillow_Boxes, name='auto-parts-boxes-detail'),
    path('pizza-boxes-detail', Pillow_Boxes, name='pizza-boxes-detail'),

]