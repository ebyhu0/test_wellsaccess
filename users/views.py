from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from .models import Contact, Department, Department_Department, Address, Phone, Email, Organization, Photo

from . import forms as userforms

from django_tables2 import RequestConfig
from django_tables2.views import SingleTableMixin, SingleTableView
from django.views.generic.edit import FormMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .tables import DepartmentTable, ContactTable, AddressTable


import django_filters
from django_filters.views import FilterView

from .filters import ContactFilter, DepartmentFilter, AddressFilter


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


class CreateContact(CreateView):
    model = Contact
    form_class = userforms.contact_create_form
    template_name = 'users/contact.html'
    # success_url = '/'
    success_url = '../contacts'  # works as a relative path from current
    success_url = '/contacts'


class CreateAddress(CreateView):
    model = Address
    form_class = userforms.address_create_form
    template_name = 'users/contact.html'
    # success_url = '/'
    success_url = '../contacts'  # works as a relative path from current
    success_url = '/filteredaddresslist'


class UpdateContactView(UpdateView):
    model = Contact
    form_class = userforms.contact_create_form
    template_name = 'users/contact.html'
    # success_url = '/'
    success_url = '../contacts'  # works as a relative path from current
    success_url = '/filteredcontactslist/'


class DetailContactView(FormMixin, DetailView):
    queryset = queryset = Contact.objects.all()
    # model = Contact
    form_class = userforms.contact_create_form
    template_name = 'users/contact.html'
    # success_url = '/'
    success_url = '../contacts'  # works as a relative path from current
    success_url = '/filteredcontactslist'

    # def get_context_data(self, **kwargs):
    #     context = super(DetailContactView, self).get_context_data(**kwargs)
    #     context['form'] = userforms.contact_create_form()
    #     return context
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()  # assign the object to the view
    #     form = self.get_form()
    #     if form.is_valid():
    #         # email = form.cleaned_data.get("email")
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class UpdateAddressView(UpdateView):
    model = Address
    form_class = userforms.address_create_form
    template_name = 'users/contact.html'
    # success_url = '/'
    success_url = '../contacts'  # works as a relative path from current
    success_url = '/filteredaddresslist'


class CreateDepartment(CreateView):
    model = Department
    form_class = userforms.department_create_form
    template_name = 'users/department.html'
    success_url = '/'


def ContactTableViewf(request):
    qs = Contact.objects.all()
    xx = ContactTable(qs)
    RequestConfig(request, paginate={"per_page": 3}).configure(xx)
    return render(request, "users/department_list.html", {"table": xx})


def DepartmentTableViewf(request):
    qs = Department.objects.all()
    xx = DepartmentTable(qs)
    RequestConfig(request, paginate={"per_page": 3}).configure(xx)
    # RequestConfig: configures one or more djangotable2
    return render(request, "users/department_list.html", {"table": xx, "objects_name": "Departmensts"})


class ContactTableViewFilter(SingleTableMixin, FilterView):
    table_class = ContactTable
    model = Contact
    template_name = 'users/table_list.html'
    filterset_class = ContactFilter  # WellsFilter
    paginate_by = 35
    success_url = '/filteredcontslist'


class AddressTableViewFilter(SingleTableMixin, FilterView):
    table_class = AddressTable
    model = Address
    template_name = 'users/table_list.html'
    filterset_class = AddressFilter  # WellsFilter
    paginate_by = 35
    success_url = '/filteredaddresslist'


class ContactTableView(SingleTableView):
    table_class = ContactTable
    model = Contact
    template_name = 'users/table_list.html'
    # filterset_class = WellsConcFilter  # WellsFilter
    paginate_by = 35

    # def form_valid(self, form):

    #     if self.request.method == 'POST':
    #         self.object = form.save()
    #         self.object = form.save(commit=False)
    #         # self.parent.add(self.object)

    #         # context = self.get_context_data(object=self.object)

    #         # formset = context['formset']

    #         if form.is_valid():
    #             self.object.save()
    #             # self.parent.save()
    #             form.save()
    # formset = wellforms.ApprovedFormSet(self.request.POST)

    # formset3.save()

    # def save(self, *args, **kwargs):
    #     dept = Department.objects.get(pk=1)
    #     self.parent.add(dept)

    # def save_related(self, request, form, formsets, change):
    #     super(ModelAdmin, self).save_related(request, form, formsets, change)
    #     category = Category.objects.get(pk=1)
    #     form.instance.categories.add(category)

    # class Department(CreateView):
    #     model = Department
    #     form_class = userforms.department_create_form
    #     template_name = 'users/department_list.html'
    #     success_url = '/'

    # def form_valid(self, form):

    #     if self.request.method == 'POST':
    #         self.object = form.save()
    #         self.object = form.save(commit=False)
    #         # self.parent.add(self.object)

    #         # context = self.get_context_data(object=self.object)

    #         # formset = context['formset']

    #         if form.is_valid():
    #             self.object.save()
    #             # self.parent.save()
    #             form.save()
    # formset = wellforms.ApprovedFormSet(self.request.POST)

    # formset3.save()

    # def save(self, *args, **kwargs):
    #     dept = Department.objects.get(pk=1)
    #     self.parent.add(dept)

    # def save_related(self, request, form, formsets, change):
    #     super(ModelAdmin, self).save_related(request, form, formsets, change)
    #     category = Category.objects.get(pk=1)
    #     form.instance.categories.add(category)


# def Department_table_filter(request):
#     # queryset=WellGeoinfo.objects.select_related().all()
#     queryset = Department.objects.all()
#     f = DepartmentFilter(request.GET, queryset=queryset)
#     table = DepartmentTable(f.qs)
#     table.request = request
#     # print("ddf")

#     # print ("request.user.group No User",request.user)

#     # if request.user.is_authenticated:

#     #     if not (request.user.groups.filter(name='geomatics_can_delete').exists()):
#     #         # print ("request.user:::::::::: ",request.user.username)
#     #         table.exclude = ('delete')
#     # else:
#     #     table.exclude = ('add_to_list', 'select_chkbox', 'delete')
#     # # table.exclud', {'table': table, 'filter': f})


class Department_update(UpdateView):
    model = Department
    form_class = userforms.department_create_form
    template_name = 'users/department.html'
    success_url = '/'

    # def form_valid(self, form):

    #     if self.request.method == 'POST':
    #         self.object = form.save()
    #         self.object = form.save(commit=False)
    #         # self.parent.add(self.object)

    #         # context = self.get_context_data(object=self.object)

    #         # formset = context['formset']

    #         if form.is_valid():
    #             self.object.save()
    #             # self.parent.save()
    #             form.save()
    # formset = wellforms.ApprovedFormSet(self.request.POST)

    # formset3.save()

    # def save(self, *args, **kwargs):
    #     dept = Department.objects.get(pk=1)
    #     self.parent.add(dept)

    # def save_related(self, request, form, formsets, change):
    #     super(ModelAdmin, self).save_related(request, form, formsets, change)
    #     category = Category.objects.get(pk=1)
    #     form.instance.categories.add(category)
