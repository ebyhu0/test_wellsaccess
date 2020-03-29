import django_filters
from .models import Department, Contact, Address


class DepartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Department

        # fields = (
        #     'concession',
        #     'exploration_name',
        #     'app_id__app_name',
        # )
        fields = {

            'name': ['icontains'],
            'organization__name': ['icontains'],
        }


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        # BeforeDate=django_filters.DateFilter(
        #     'birth_date', lookup_type=''
        # )

        # fields = (
        #     'concession',
        #     'exploration_name',
        #     'app_id__app_name',
        # )
        fields = {

            'first_name': ['icontains'],
            'middle_name': ['icontains'],
            'last_name': ['icontains'],
            # 'birth_date': ['icontains'],

            # 'organization__name': ['icontains'],
        }


class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        # BeforeDate=django_filters.DateFilter(
        #     'birth_date', lookup_type=''
        # )

        # fields = (
        #     'concession',
        #     'exploration_name',
        #     'app_id__app_name',
        # )
        fields = {

            'address': ['icontains'],
            'district': ['icontains'],
            'zip_code': ['icontains'],
            # 'birth_date': ['icontains'],

            # 'organization__name': ['icontains'],
        }
