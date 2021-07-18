from django.shortcuts import render, redirect

from .forms import BooksForm
from .models import Books


def show_books(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_books(request):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    context = {
        'form': form
    }
    return render(request, "add_book_form.html", context)
