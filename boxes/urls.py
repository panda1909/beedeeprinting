from django.urls import path, include
from .views import Pillow_Boxes, Gable_Boxes, Windows_Boxes, Mailer_Boxes, Kraft_Boxes, Cosmetics_Boxes, Display_Boxes, Sleeve_Boxes, Beverages_Boxes, Candle_Boxes, Autoparts_Boxes, Pizza_Boxes

app_name='boxes'

urlpatterns = [
    path('pillow-boxes-detail', Pillow_Boxes, name='pillow-boxes-detail'),
    path('gable-boxes-detail', Gable_Boxes, name='gable-boxes-detail'),
    path('window-boxes-detail', Windows_Boxes, name='window-boxes-detail'),
    path('mailer-boxes-detail', Mailer_Boxes, name='mailer-boxes-detail'),
    path('kraft-boxes-detail', Kraft_Boxes, name='kraft-boxes-detail'),
    path('cosmetics-boxes-detail', Cosmetics_Boxes, name='cosmetics-boxes-detail'),
    path('display-boxes-detail', Display_Boxes, name='display-boxes-detail'),
    path('sleeve-boxes-detail', Sleeve_Boxes, name='sleeve-boxes-detail'),
    path('beverage-boxes-detail', Beverages_Boxes, name='beverage-boxes-detail'),
    path('candle-boxes-detail', Candle_Boxes, name='candle-boxes-detail'),
    path('auto-parts-boxes-detail', Autoparts_Boxes, name='auto-parts-boxes-detail'),
    path('pizza-boxes-detail', Pizza_Boxes, name='pizza-boxes-detail'),

]