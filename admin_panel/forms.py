from django import forms
from .models import Author, Genre, Type

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
    
