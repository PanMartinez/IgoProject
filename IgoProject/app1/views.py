from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.template.response import TemplateResponse
from .models import Company, Comment
from .forms import AddCompanyForm, CreateCommentForm


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


class CompanyDetailsView(LoginRequiredMixin, DetailView):
    """
    View of company details with comment button on the bottom
    """
    model = Company
    template_name = 'company_details.html'


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


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    template_name = 'form_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.company = Company.objects.get(pk=self.kwargs["company_id"])
        return super(CreateCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('company_details', kwargs={'pk': self.object.company.id})


