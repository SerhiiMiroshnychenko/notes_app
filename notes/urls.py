from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', get_notes_list),  # Прив'язка функції index до URL запиту на головну сторінку
    path('', NotesListView.as_view(), name='home'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('addcat/', AddCat.as_view(), name='add_cat'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('post/<int:post_id>/edit', edit_note, name='edit'),
    path('post/<int:post_id>/delete', delete_note, name='delete'),
    path('search/', SearchListView.as_view(), name='search'),
]
