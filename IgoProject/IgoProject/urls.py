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

from app1.views import (
    StartView,
    CompaniesListView,
    CompanyDetailsView,
    AddCompanyView,
    UsersListView,
    CompanyUpdateView,
    CompanyDeleteView,
    CreateCommentView,
    UpdateUserView,
    DeleteUserView,
    DashboardView,
    register

)


urlpatterns = [
                  url(r'^admin/', include(admin.site.urls), name="admin"),

                  # log urls
                  url(r'^login/$', auth_views.login, {'template_name': 'login_form.html'}, name='login'),
                  url(r'^logout/$', auth_views.logout, {"next_page": "login"}, name='logout'),
                  url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'password_reset_form.html'},
                      name='password_reset'),
                  url(r'^password_reset/done/$', auth_views.password_reset_done,
                      {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
                  url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                      auth_views.password_reset_confirm, {'template_name': 'password_reset_confirm.html'},
                      name='password_reset_confirm'),
                  url(r'^reset/done/$', auth_views.password_reset_complete,
                      {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),

                  # CRM url
                  url(r'^index', StartView.as_view(), name="home"),
                  url(r'^companies_list/', CompaniesListView.as_view(), name="companies_list"),
                  url(r'^company_details/(?P<pk>(\d)+)', CompanyDetailsView.as_view(), name='company_details'),
                  url(r'add_company/', AddCompanyView.as_view(), name="add_company"),
                  url(r'^company/(?P<pk>(\d)+)/edit$', CompanyUpdateView.as_view(), name="company_update"),
                  url(r'^company/(?P<pk>(\d)+)/delete$', CompanyDeleteView.as_view(), name="company_delete"),
                  url(r'users_list/', UsersListView.as_view(), name="users_list"),
                  url(r'^register/$', register, name='register'),

                  url(r'^user/(?P<pk>(\d)+)/edit$', UpdateUserView.as_view(), name="user_update"),
                  url(r'^user/(?P<pk>(\d)+)/delete$', DeleteUserView.as_view(), name="user_delete"),

                  url(r'^add_comment/(?P<company_id>(\d)+)', CreateCommentView.as_view(), name='comment'),
                  url(r'^dashboard/', DashboardView.as_view(), name="dashboard"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
