from django import forms
from .models import Author, Genre, Type, Book

# Book
class BookForm(forms.ModelForm):
    first_release_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    latest_release_date = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 4}))
    prologue = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 4}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False, widget=forms.Select(attrs={'class': 'select2'}))
    co_authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'select2'}))
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), required=False, widget=forms.Select(attrs={'class': 'select2'}),empty_label="None")
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False, widget=forms.SelectMultiple(attrs={'class': 'select2'}))
    cover_photo = forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control',}),)
    class Meta:
        model = Book
        fields = '__all__'

    

# Authorss
class AuthorForm(forms.ModelForm):
    dob = forms.DateField(required=False,widget=forms.DateInput(attrs={'type': 'date'}))
    bio = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Author
        fields = ['name', 'dob','bio','country','image']

# Genre
class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

# Type
class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']


    
