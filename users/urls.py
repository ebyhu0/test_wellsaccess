"""wells_access URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views as user_views


urlpatterns = [

    path('contact/',  user_views.CreateContact.as_view(), name='contact'),
    path('contacts/',  user_views.ContactTableViewf, name='contacts'),
    path('contactslist/',  user_views.ContactTableView.as_view(), name='contactslist'),
    path('contactupdate/<pk>',  user_views.UpdateContactView.as_view(),
         name='contact-update'),
    path('contactdetail/<pk>',  user_views.DetailContactView.as_view(),
         name='contact-detail'),
    path('filteredcontactslist/',  user_views.ContactTableViewFilter.as_view(),
         name='filteredcontacts'),

    path('createaddress/',  user_views.CreateAddress.as_view(), name='createcontact'),

    path('addressupdate/<pk>',  user_views.UpdateAddressView.as_view(),
         name='address-update'),
    path('filteredaddresslist/',  user_views.AddressTableViewFilter.as_view(),
         name='filteredaddresses'),



    path('department/',  user_views.CreateDepartment.as_view(), name='department'),

    path('departments/',  user_views.DepartmentTableViewf, name='departments'),

    # path('departmentlist/',  user_views.Department_List.as_view(),
    #      name='department-list'),

    path('depupdate/<pk>',  user_views.Department_update.as_view(),
         name='department_update'),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

# if settings.MEDIA_URL:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
