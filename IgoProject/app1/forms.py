from django import forms
from django.contrib.auth.models import User
from .models import Company



class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
