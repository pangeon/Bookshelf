from django.shortcuts import render, redirect

from .forms import BooksForm
from .models import Books, Bibliographies, BooksGenres


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
    bibliography = None
    book_genre = None
    error = None

    try:
        bibliography = Bibliographies.objects.get(bibliography_fk=book)
        book_genre = BooksGenres.objects.get(book_genre_fk=book)
    except Exception as e:
        error = f"SYSTEM: {e} " \
                f"DESCRIPTION: The book does not contain reference to bibliography or genre data."

    context = {
        'book': book,
        'bibliography': bibliography,
        'book_genre': book_genre,
        'error': error
    }

    return render(request, 'book_details.html', context)