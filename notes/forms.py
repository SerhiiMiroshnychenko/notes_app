from django import forms
from django.core.exceptions import ValidationError
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категорія не обрана"

    class Meta:
        model = Note  # Зв'язуємо ModelForm з моделлю Note
        # fields - список полів, які треба відтворити
        fields = ['title', 'text', 'reminder', 'category']
        #  widgets - індивідуальні стилі для полів
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        # Метод для користувацького валідатора. Повинен починатися з "clean_"
        title = self.cleaned_data['title']  # Отримаємо заголовок який ввів користувач
        if len(title) > 200:
            raise ValidationError('Довжина більша 200 символів')

        return title


class AddCatForm(forms.ModelForm):

    class Meta:
        model = Category
        # fields - список полів, які треба відтворити
        fields = '__all__'
        #  widgets - індивідуальні стилі для полів
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def clean_title(self):
        # Метод для користувацького валідатора. Повинен починатися з "clean_"
        title = self.cleaned_data['title']  # Отримаємо заголовок який ввів користувач
        if len(title) > 200:
            raise ValidationError('Довжина більша 200 символів')

        return title


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'category']



