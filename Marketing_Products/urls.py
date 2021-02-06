from django.urls import path, include
from .views import Calendars_detail, Broucher_Flyers_Detail , Postcard_Detail, Hangtags_Detail, Laberlsandstickers_Detail, NCRforms_Detail, Presentation_folder_Detail, Custom_holiday_cards_Detail
app_name = 'Marketing_Products'

urlpatterns = [
    path('calenders-detail', Calendars_detail, name= 'calenders-detail'),
    path('brouchers-flyers-detail', Broucher_Flyers_Detail, name='brouchers-flyers-detail'),
    path('postcards-detail', Postcard_Detail, name= 'postcards-detail'),
    path('hangtags-detail', Hangtags_Detail, name='hangtags-detail'),
    path('labels-and-stickers-detail', Laberlsandstickers_Detail, name='labels-and-stickers-detail'),
    path('ncr-forms-detail', NCRforms_Detail, name= 'ncr-forms-detail'),
    path('presentation-folder-detail', Presentation_folder_Detail, name='presentation-folder-detail'),
    path('custom-holiday-cards-detail', Custom_holiday_cards_Detail, name='custom-holiday-cards-detail'),
]
