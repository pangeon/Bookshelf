
from django import forms

from .models import Books


class BooksForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter book title'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter book author'}))

    class Meta:
        model = Books
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        unacceptable_characters = \
            ["@", "#", "$", "^", "&", "*", "(", ")", "[", "]", "<", ">", "/"]
        for letter in unacceptable_characters:
            if str(title).find(letter) is not -1:
                raise forms.ValidationError("Unacceptable characters in data form.")

        return title

    def check_author(self):
        author = self.cleaned_data.get('author')
        unacceptable_characters = \
            ["@", "#", "$", "^", "&", "*", "(", ")", "[", "]", "<", ">", "/"]
        for letter in unacceptable_characters:
            if str(author).find(letter) is not -1:
                raise forms.ValidationError("Unacceptable characters in data form.")

        return author

