from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BooksForm
from .models import Books, Bibliographies, BooksGenres


def show_books(request):
    books = Books.objects.all()
    return render(request, 'book_list.html', {'books': books, 'name': 'Catalog'})


def add_books(request):
    if not request.user.is_authenticated:
        context = {
            'info': "Probably you do not have access to resources, please register and login.",
            'exception': ''
        }
        return render(request, "401.html", context)

    form = BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("books_list")
    context = {
        'form': form
    }
    return render(request, "add_book_form.html", context)


def show_book_for_id(request, book_id):
    try:
        book = get_object_or_404(Books, id=book_id)
        bibliography = get_object_or_404(Bibliographies, bibliography_fk=book)
        book_genre = get_object_or_404(BooksGenres, book_genre_fk=book)

        context = {
            'book': book,
            'bibliography': bibliography,
            'book_genre': book_genre,
        }
        return render(request, 'book_details.html', context)
    except Http404 as e:
        context = {
            'info': "Probably the resource you are looking for does not exist",
            'exception': e
        }
        return render(request, "404.html", context)


