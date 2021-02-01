from django.urls import path, include
from .views import Envelops_detail, Letterhead_detail, Notepad_detail

app_name='Business_Stationary'

urlpatterns = [
    path('envelopes-detail', Envelops_detail, name='envelopes-detail'),
    path('letterhead-detail', Letterhead_detail, name='letterhead-detail'),
    path('notepad-detail', Notepad_detail, name='notepad-detail'),
]
