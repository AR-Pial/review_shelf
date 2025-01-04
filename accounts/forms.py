from django import forms
from .models import CustomUserModel
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django_countries.fields import CountryField

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    first_name = forms.CharField(required=True) 
    country = CountryField().formfield(required=True)

    class Meta:
        model = CustomUserModel
        fields = ['first_name','last_name','email','country', 'password','confirm_password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)  # Validate password using Django's password validators
        except ValidationError as e:
            raise ValidationError(e.messages)  # Re-raise error if validation fails
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return confirm_password
