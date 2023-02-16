from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Note(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=10000)
    reminder = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='note_category')
