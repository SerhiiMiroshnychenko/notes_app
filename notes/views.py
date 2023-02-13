from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # Функція, що імплементує цей конкретний view
    # Щоби ця функція спрацювала, вона повинна бути прив'язана дор якогось запиту URL
    return HttpResponse("Hello from Notes app and Serhii Miroshnychenko.")
    # HttpResponse -> функція, що повертає в браузер текстову відповідь,
    # передану їй як аргумент
