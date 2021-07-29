from django import forms

from .models import Books, Bibliographies, BooksGenres


# ! Method must be name clean_ (...)
class BooksForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter book title'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter book author'}))

    class Meta:
        model = Books
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        BooksForm.has_unacceptable_characters(title)
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        BooksForm.has_unacceptable_characters(author)
        return author

    @staticmethod
    def has_unacceptable_characters(field):
        unacceptable_characters = \
            ["@", "#", "$", "^", "&", "*", "(", ")", "[", "]", "<", ">", "/"]
        for letter in unacceptable_characters:
            if str(field).find(letter) is not -1:
                raise forms.ValidationError("Unacceptable characters in data form.")


class BibliographyForm(forms.ModelForm):
    language = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Set book language symbol'}))
    publishing_house = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add publishing house'}))
    publication_place = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add publication place'}))
    publication_year = forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}))

    class Meta:
        model = Bibliographies
        fields = [
            'language',
            'publishing_house',
            'publication_place',
            'publication_year',
            'bibliography_fk'
        ]


class BooksGenresForm(forms.ModelForm):
    CHOICES = []
    book_genres = BooksGenres.objects.all()

    for item in book_genres:
        CHOICES.append((item.id, item.name))

    name = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = BooksGenres
        fields = [
            'book_genre_fk'
        ]
