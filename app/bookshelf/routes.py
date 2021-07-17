from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.show_books),
    path('/add', views.add_books),
]