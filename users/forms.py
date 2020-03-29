from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Contact, Department, Address
from django.forms import ModelForm

from crispy_forms.helper import FormHelper


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class contact_create_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super(contact_create_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        instance = getattr(self, 'instance', None)

    class Meta:
        model = Contact
        # readonly_fields = ['well_id','well_status',]
        exclude = ['middle_name']
        # fields = ['first_name', 'middle_name', 'last_name', 'birth_date']


class address_create_form(ModelForm):

    def __init__(self, *args, **kwargs):
        super(address_create_form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)

    class Meta:
        model = Address
        # readonly_fields = ['well_id','well_status',]
        exclude = ['id']
        # fields = []


class department_create_form(ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(department_create_form, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)

    # # def form_valid(self,form):
    # #     obj=form.save()
    # #     for pp in self.request.POST.getlist('Department'):
    # #         obj.save(commit=False)

    # def save(self):
    #     xx = department_create_form.save(self)
    #     xx.save_m2m()

    class Meta:
        model = Department
        exclude = ['id', ]
        # readonly_fields = ['well_id','well_status',]

        # fields = ['id', 'name', 'organization']
