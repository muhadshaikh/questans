from django import forms
from .modelss import Register

class RegisterForm(forms.ModelForm):
    class meta:
        model = Register
        fields="__all__"
