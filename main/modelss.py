from django import forms
from django.core import validators


class Register(forms.Form):
    first_name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    last_name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(max_length=15)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()