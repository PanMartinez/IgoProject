from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Company, Comment



class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'slainteet': forms.HiddenInput,
}