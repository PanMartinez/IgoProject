"""IgoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from app1 import views as core_views

from app1.views import (
    StartView,
    CompaniesListView,
    CompanyDetailsView,
    AddCompanyView,
    UsersListView,
    CompanyUpdateView
)

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),

                  # log urls
                  url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
                  url(r'^logout/$', auth_views.logout, {"next_page": "login"}, name='logout'),
                  url(r'^signup/$', core_views.signup, name='signup'),

                  # CRM urls
                  url(r'^index', StartView.as_view(), name="home"),
                  url(r'^companies_list/', CompaniesListView.as_view(), name="companies_list"),
                  url(r'company_details/(?P<company_id>(\d)+)$', CompanyDetailsView.as_view(), name="company_details"),
                  url(r'add_company/', AddCompanyView.as_view(), name="add_company"),
                  url(r'users_list/', UsersListView.as_view(), name="users_list"),
                  url(r'^company/(?P<pk>(\d)+)/edit$', CompanyUpdateView.as_view(), name="company_update"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
