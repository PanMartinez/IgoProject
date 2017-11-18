from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.template.response import TemplateResponse
from .models import Company
from .forms import SignUpForm, AddCompanyForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class StartView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "index.html")


class CompaniesListView(LoginRequiredMixin, View):
    def get(self, request):
        return TemplateResponse(request, 'companies_list.html')


class CompanyDetailsView(LoginRequiredMixin, View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        return render(request, "company_details.html", {"company": company})


class AddCompanyView(LoginRequiredMixin, CreateView):
    form_class = AddCompanyForm
    template_name = "form.html"
    success_url = reverse_lazy("companies_list")


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy("companies_list")


class UsersListView(LoginRequiredMixin, View):
    def get(self, request):
        return TemplateResponse(request, "users_list.html")
