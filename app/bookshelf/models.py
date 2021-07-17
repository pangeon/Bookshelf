from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.author} <> \"{self.title}\""


class Bibliographies(models.Model):
    language = models.CharField(max_length=3)
    publishing_house = models.CharField(max_length=100)
    publication_place = models.CharField(max_length=200)
    publication_year = models.DateTimeField()

    original_title = models.CharField(max_length=200, null=True, blank=True)
    origin_publishing_house = models.CharField(max_length=100, null=True, blank=True)
    origin_publication_place = models.CharField(max_length=200, null=True, blank=True)
    translators = models.CharField(max_length=200, null=True, blank=True)
    additional_creators = models.TextField(null=True, blank=True)
    numbers_of_pages = models.IntegerField(null=True, blank=True)
    release = models.IntegerField(null=True, blank=True)
    ISBN = models.CharField(max_length=13, null=True, blank=True)
    bibliography_fk = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Bibliographies"

    def __str__(self):
        return f"{self.publishing_house}, {self.publication_place}, {self.publication_year.year}"


class BooksGenres(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=8)
    description = models.TextField(null=True, blank=True)
    book_genre_fk = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "BooksGenres"

    def __str__(self):
        return f"{self.name}"
