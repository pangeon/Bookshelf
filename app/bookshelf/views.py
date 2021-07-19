from django.shortcuts import render, redirect

from .forms import BooksForm
from .models import Books, Bibliographies


def show_books(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books, 'name': 'Catalog'})


def add_books(request):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("books_list")
    context = {
        'form': form
    }
    return render(request, "add_book_form.html", context)


def show_book_for_id(request, book_id):
    book = Books.objects.get(id=book_id)
    bibliography = Bibliographies.objects.get(book=book)

    context = {
        'book': book,
        'bibliography': bibliography
    }

    return render(request, 'book_details.html', context)