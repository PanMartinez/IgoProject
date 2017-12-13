from django import forms
from django.contrib.auth.models import User
from .models import Company, Comment


class RegistrationForm(forms.Form):
    first_name = forms.RegexField(regex=r'^\w+$',
                                  widget=forms.TextInput(attrs=dict(required=False, max_length=30, placeholder="Jules")),
                                  label=("First name"),
                                  error_messages={'invalid': ("Only letters, numbers and undescores avaiable.")})
    last_name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs=dict(required=True, max_length=30, placeholder="Winnfield")), label=("Last name"),
                                 error_messages={'invalid': ("Only letters, numbers and undescores avaiable.")})
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs=dict(required=True, max_length=30, placeholder="BadMfcr")), label=("Username"),
                                error_messages={'invalid':("Only letters, numbers and undescores avaiable.")})
    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(required=True, max_length=30, placeholder="badmr@kahuna.com")),
        label=("Email address"))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("This username already exists.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Password's didn't match")
        return self.cleaned_data


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("title", "content")
