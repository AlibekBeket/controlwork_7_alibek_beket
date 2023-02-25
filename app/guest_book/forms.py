from django import forms
from django.core.exceptions import ValidationError

from guest_book.models import GuestBook


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ("author_name", "author_email", "text")
        labels = {
            'author_name': 'Имя',
            'author_email': 'Email',
            'text': 'Текст'
        }

    def clean_author_name(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 3:
            raise ValidationError('Имя не может состоять из 1 или 2 символов')
        return author_name

    def clean_author_email(self):
        author_email = self.cleaned_data.get('author_email')
        if len(author_email) < 3:
            raise ValidationError('Почта не может состоять из 1 или 2 символов')
        return author_email

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 5:
            raise ValidationError('Текст не может состоять из 1 или 2 символов')
        return text


class GuestFind(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))

    def clean_name(self):
        author_name = self.cleaned_data.get('name')
        if len(author_name) < 3:
            raise ValidationError('Имя не может состоять из 1 или 2 символов')
        return author_name
