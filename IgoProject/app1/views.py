from django.shortcuts import render

# Create your views here.


class CompaniesListView(View):
    def get (self, request):
        return TemplateResponse(request, 'companies_list.html')


class CompanyDetailsView(View):
    def get (self, request, book_id):
        book = Book.objects.get(id = book_id)
        return render( request, "company_details.html", {"company": company})


class AddCompanyView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'app1.add_company'
    form_class = AddCompanyForm
    template_name = "add_company.html"
    success_url = reverse_lazy("companies_list")