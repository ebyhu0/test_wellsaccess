from django.utils.html import format_html
from django.template import RequestContext


import django_tables2 as tables
from django_tables2.utils import A
from django_tables2 import SingleTableView

from django.urls import reverse


from .models import Profile, Department, Contact, Department_Department, Organization, Photo, Address, Phone, Email, Country, Identity

from wells import views


class DepartmentTable(tables.Table):
    name = tables.LinkColumn('department_update', args=[A('pk')])

    class Meta:
        model = Department
        exclude = ('id',)
        # fields = ('id','concession','concessiontype',
        #           'isactive','area_km2',
        #           'operator')

        attrs = {"class": "table-striped table-bordered", 'width': '100%'}
        empty_text = "There are no department matching the search criteria..."
        # row_attrs = {
        #     'conc-id': lambda record: record.pk
        # }


class ContactTable(tables.Table):
    first_name = tables.LinkColumn('contact-update', args=[A('pk')])

    class Meta:
        model = Contact

        exclude = ('id',)
        # fields = ('id','concession','concessiontype',
        #           'isactive','area_km2',
        #           'operator')

        attrs = {"class": "table-striped table-bordered", 'width': '100%'}
        empty_text = "There are no Contacts matching the search criteria..."
        # row_attrs = {
        #     'conc-id': lambda record: record.pk
        # }


class AddressTable(tables.Table):
    address = tables.LinkColumn('address-update', args=[A('pk')])

    class Meta:
        model = Address

        exclude = ('id',)
        # fields = ('id','concession','concessiontype',
        #           'isactive','area_km2',
        #           'operator')

        attrs = {"class": "table-striped table-bordered", 'width': '100%'}
        empty_text = "There are no Contacts matching the search criteria..."
        # row_attrs = {
        #     'conc-id': lambda record: record.pk
        # }
