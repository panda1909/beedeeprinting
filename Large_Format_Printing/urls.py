from django.urls import path, include
from .views import FoamCorePostersDetail

urlpatterns = [
    path('', FoamCorePostersDetail, name= 'FoamCorePosters'),
]
