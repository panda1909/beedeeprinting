from django.urls import path, include
from .views import Foamcore_poster_detail, Poster_printing_detail, Retractable_banners_detail, Table_covers_detail, Floor_stickers_detail
app_name = 'Large_Format_Printing'
urlpatterns = [
    path('foamcore-poster-detail', Foamcore_poster_detail, name= 'foamcore-poster-detail'),
    path('poster-printing-detail', Poster_printing_detail, name='poster-printing-detail'),
    path('retractable-banners-detail', Retractable_banners_detail, name= 'retractable-banners-detail'),
    path('table-cover-detail', Table_covers_detail, name= 'table-cover-detail'),
    path('floor-stickers-detail', Floor_stickers_detail, name='floor-stickers-detail'),
]
