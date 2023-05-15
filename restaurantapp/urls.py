from django.urls import path
from .views import  *


urlpatterns = [
    
    path("home", index),
    path('unit', unit, name="unit"),
   
]
