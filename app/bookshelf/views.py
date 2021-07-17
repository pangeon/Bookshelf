from django.shortcuts import render

from .forms import BooksForm
from .models import Books


def show_books(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_books(request):
    form = BooksForm()
    context = {
        'form': form
    }
    return render(request, 'add_book_form.html', context)
