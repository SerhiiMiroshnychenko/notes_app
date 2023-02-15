from django.shortcuts import render
from django.http import HttpResponse

my_notes = ['Нотатка 1', 'Нотатка 2', 'Нотатка 3']


# Create your views here.
def index(request):
    return render(request, 'notes/index.html',
                  {'title': 'Додаток NOTES', 'my_notes': my_notes})
