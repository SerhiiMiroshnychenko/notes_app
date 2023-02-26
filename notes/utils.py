from django.db.models import Count
from .models import *


menu = [{'title': "Про сайт", 'url_name': 'home'},
        {'title': "Додати статтю", 'url_name': 'add_page'},
        {'title': "Категорії", 'url_name': 'notes'},
        {'title': "Category", 'url_name': 'cats'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('id'))

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
