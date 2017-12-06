from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.template.response import TemplateResponse
from .models import Company
from .forms import AddCompanyForm


# Create your views here.



class StartView(LoginRequiredMixin, View):
    """
    Starting View with welcome message
    """
    def get(self, request):
        return render(request, "index.html")


class CompaniesListView(LoginRequiredMixin, View):
    """
    View displaying  list of all added companies, with details, edit and delete buttons.
    Add of a new company is also possible.
    """
    def get(self, request):

        return TemplateResponse(request, 'companies_list.html')


class CompanyDetailsView(LoginRequiredMixin, View):
    """
    View of company details
    """
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        return render(request, "company_details.html", {"company": company})


class AddCompanyView(LoginRequiredMixin, CreateView):
    """
    New company view
    """
    form_class = AddCompanyForm
    template_name = "form.html"
    success_url = reverse_lazy("companies_list")


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """
    Company edit view
    """
    model = Company
    fields = '__all__'
    template_name = "form.html"
    success_url = reverse_lazy("companies_list")


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = "delete.html"
    success_url = reverse_lazy("companies_list")


class UsersListView(LoginRequiredMixin, View):
    """
    users list view
    """
    def get(self, request):
        return TemplateResponse(request, "users_list.html")
