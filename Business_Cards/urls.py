from django.urls import path, include
from .views import Edge_painted_Detail, BC_Detail

app_name='Business_Cards'

urlpatterns = [
    path('edge-painted-detail', Edge_painted_Detail, name='edge-painted-detail'),
    path('business-card-detail', BC_Detail, name='business-card-detail'),

]
