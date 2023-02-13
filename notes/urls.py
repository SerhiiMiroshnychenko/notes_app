from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('hello/', index),  # Прив'язка функції index до URL запиту за адресою hello/
]
