from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('', index),  # Прив'язка функції index до URL запиту на головну сторінку
]
