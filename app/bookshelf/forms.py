from django.forms import models

from .models import Books


class BooksForm(models.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author']