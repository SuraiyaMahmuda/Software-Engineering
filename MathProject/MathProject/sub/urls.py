from django.urls import path
from . import views

urlpatterns = [
    path('', views.subtract_numbers, name='subtract_numbers'), #Subtract
]