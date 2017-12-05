core Django imports
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views

#Import from current app
from . import views

app_name = 'app1'

urlpatterns=[
    #login views
    url(r'^login/$', auth_views.login, {'template_name': 'registration/fullscreen_login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'registration/password_reset_form.html'}, name='password_reset'),
    url(r'^logout/$', views.logout_crm, name="logout"),
    # CRM url
    url(r'^index', StartView.as_view(), name="home"),
    url(r'^companies_list/', CompaniesListView.as_view(), name="companies_list"),
    url(r'company_details/(?P<company_id>(\d)+)$', CompanyDetailsView.as_view(), name="company_details"),
    url(r'add_company/', AddCompanyView.as_view(), name="add_company"),
    url(r'users_list/', UsersListView.as_view(), name="users_list"),
    url(r'^company/(?P<pk>(\d)+)/edit$', CompanyUpdateView.as_view(), name="company_update"),
    url(r'^company/(?P<pk>(\d)+)/delete$', CompanyDeleteView.as_view(), name="company_delete")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)