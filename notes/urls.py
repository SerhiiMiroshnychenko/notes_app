from django.contrib import admin
from django.urls import path
from .views import get_notes_list

urlpatterns = [
    path('', get_notes_list),  # Прив'язка функції index до URL запиту на головну сторінку
]
