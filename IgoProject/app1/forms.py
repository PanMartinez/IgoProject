from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional field')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional field')
    email = forms.EmailField(max_length=254, help_text='Field required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
