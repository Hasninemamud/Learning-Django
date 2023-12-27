from django.urls import path
from . import views



urlpatterns = [
    path('bk', views.bkash),
    path('rock', views.rocket)
    
    
]