from django import forms
from carsapp.models import Signup
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Signup
        fields = ['first_name','last_name','username','email','password1','password2']