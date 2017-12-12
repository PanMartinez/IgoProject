from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.template.response import TemplateResponse
from .models import Company, Comment, User
from .forms import AddCompanyForm, RegistrationForm

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, user_passes_test



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
    template_name = "form_company.html"
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
    template_name = "company_delete.html"
    success_url = reverse_lazy("companies_list")
    success_message = ""

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        request.session['name'] = name
        message = 'Company' + request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(CompanyDeleteView, self).delete(request, *args, **kwargs)


class UsersListView(LoginRequiredMixin, View):
    """
    users list view
    """
    def get(self, request):
        return TemplateResponse(request, "users_list.html")


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """
    Users edit view
    """
    model = User
    fields = '__all__'
    template_name = "user_edit.html"
    success_url = reverse_lazy("users_list")


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("users_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.username
        request.session['name'] = name
        message = 'User' + request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteUserView, self).delete(request, *args, **kwargs)


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


class DashboardView(LoginRequiredMixin, View):
    """
    View displaying  list of all added companies, with details, edit and delete buttons.
    Add of a new company is also possible.
    """
    def get(self, request):

        return TemplateResponse(request, 'dashboard.html')



@csrf_protect
@login_required
@user_passes_test(lambda u: u.is_superuser) #check if the request.user is staff member if yes - allow him to register new users
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'New User successfully added')
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('users_list')
    else:
        form = RegistrationForm()

    variables = {
    'form': form
    }

    return render(request, 'user_registration.html', variables)