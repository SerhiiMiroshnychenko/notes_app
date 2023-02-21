from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=15, verbose_name='Категорія')

    class Meta:
        verbose_name = _("Категорія")
        verbose_name_plural = _("Категорії")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


class Note(models.Model):
    title = models.CharField(max_length=150, verbose_name='Назва нотатки')
    text = models.TextField(max_length=10000, verbose_name='Вміст нотатки')
    reminder = models.DateTimeField(verbose_name='Нагадування')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категорія', related_name='note_category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note', kwargs={'id': self.pk})
