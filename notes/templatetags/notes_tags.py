from django import template
from notes.models import *


register = template.Library()


@register.inclusion_tag('notes/list_categories.html')  # Шаблон куди передається словник в return-і
def show_categories(cat_selected=0):
    """
    Функція - тег включення
    Тег включення - формує та повертає фрагмент HTML сторінки
    """
    cats = Category.objects.all()  # Читає всі категорії

    return {"cats": cats, "cat_selected": cat_selected}  # Повертає словник в шаблон 'plants/list_categories.html'
