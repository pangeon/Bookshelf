from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_books, name="books_list"),
    path('/add', views.add_books, name="add_book"),
    path('/show/<int:book_id>', views.show_book_for_id, name="book_for_id"),
]