from django import forms

from .models import Books


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
