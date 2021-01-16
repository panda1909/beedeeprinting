from django.urls import path, include
from .views import Edge_painted_Detail

app_name='Business_Cards'

urlpatterns = [
    path('', Edge_painted_Detail, name='edge-painted-detail'),
]
