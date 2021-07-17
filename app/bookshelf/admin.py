from django.contrib import admin


from .models import Books, Bibliographies, BooksGenres

admin.site.register(Books)
admin.site.register(Bibliographies)
admin.site.register(BooksGenres)
