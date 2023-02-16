from django.shortcuts import render
from django.http import HttpResponse
from .models import Note


# Create your views here.
def get_notes_list(request):
    context = {'notes_list': Note.objects.all()}
    return render(request, 'notes/index.html', context)
