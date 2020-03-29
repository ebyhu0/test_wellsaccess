import time
import math
from django.conf import settings
from django.views.generic import TemplateView, FormView
from . import bap_lib
from osgeo.osr import SpatialReference, CoordinateTransformation
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.urls import reverse, reverse_lazy
from django.db.models import F


from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import RequestConfig
import django_filters
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from .filters import WellsFilter, WellsConcFilter
from django.db import transaction
from django.contrib.auth.models import User, Group
from django.forms import inlineformset_factory
from . import forms as wellforms
from django.forms import ModelForm

from .models import Concession, WellGeoinfo, Approved, Staked, Provisional, Psd
from .tables import ConcessionTable, WellGeoinfoTable, ApprovedTable
from cart.forms import CartAddItemForm
from cart.cart import Cart

from crispy_forms.utils import render_crispy_form

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def ConcWells_pp(request, pk):
    # pw=ProposedWells.objects.get(pk=pk)
    cnc = get_object_or_404(Concession, pk=pk)
    form = ConcessionModelForm(request.POST or None, instance=cnc)
    # WellNamesFormset=inlineformset_factory(ProposedWells,Wellnames,fields=('wellname_id','well_name','nametype','fk_well_id',),extra=1,can_delete=False)
    WellsFormset = inlineformset_factory(
        Concession, WellGeoinfo, form=Well_Form, extra=1, can_delete=False)

    if request.method == 'POST':
        formset = WellsFormset(request.POST, instance=cnc)

        if formset.is_valid() and form.is_valid():
            formset.save()
            form.save()

            return redirect('list-concwells', pk=cnc.pk)

    formset = WellsFormset(instance=cnc)

    return render(request, 'wells/pp_concwell.html', {'formset': formset, 'form': form})


def crispformdef(request, pk):
    # This view is missing all form handling logic for simplicity of the example
    myobject = get_object_or_404(WellGeoinfo, pk=pk)
    form = wellforms.wellDetail_form(instance=myobject)
    # print(request.session['pks'] )
    # my_var = request.session.pop('pks')
    # print(my_var)

    if request.method == "POST":
        formset = wellforms.ApprovedFormSet(request.POST, instance=myobject)
        return render(request, 'wells/wellgeoinfo_form.html', {'form': form, 'formset': formset})
    else:
        formset = wellforms.ApprovedFormSet(instance=myobject)
        return render(request, 'wells/wellgeoinfo_form.html', {'form': form, 'formset': formset})

    # return render(request, 'wells/wellgeoinfo_form.html', {'form': form})

# class crispformcls_view(UpdateView):
#     model = WellGeoinfo
#     form_class = wellforms.wellDetail_formlayout

#     def get_form(self, form_class=None):
#         if form_class is None:
#             form_class = self.get_form_class()
#         # form = self.get_form(form_class)
#         # formset =  wellforms.ApprovedFormSet(instance=self.object)
#         form = super(crispformcls_view, self).get_form()
#         # form.fields['app_id'].queryset = Approved.objects.filter(well_info=self.kwargs['pk'])
#         # return form
#         return render_crispy_form(form,"wells/wellgeoinfo_form.html", context=None)
#         # return render_crispy_form(form, helper=None, context=None)
        # return TemplateResponse(request, "wellgeoinfo_form.html", {'form': form})


class ConcstableView(ListView):
    model = Concession
    # fields = ['concession', 'area_km2',
    #           'concessiontype', 'operator', 'isactive']

    form_class = wellforms.ConcessionModelForm
    context_object_name = 'concs'
    template_name = 'wells/concs_table.html'
    # ordering = ['-exploration_name']
    ordering = ['concession']
    # group_required = u'operator'
    paginate_by = 10

    def get_queryset(self):
        qs = super(ConcstableView, self).get_queryset()
        # return qs.filter.conc_id
        return qs.filter(isactive=True).order_by('concession')

    def get_context_data(self, **kwargs):
        context = super(ConcstableView, self).get_context_data(**kwargs)
        context['nav_concession'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = ConcessionTable(self.get_queryset())
        # RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class ConcstableListView(ListView):
    model = Concession
    # fields = ['concession', 'area_km2',
    #           'concessiontype', 'operator', 'isactive']

    form_class = wellforms.ConcessionModelForm
    context_object_name = 'concs'
    template_name = 'wells/concs_tablelist.html'
    # ordering = ['-exploration_name']
    ordering = ['concession']
    # group_required = u'operator'
    paginate_by = 200

    def get_queryset(self):
        qs = super(ConcstableListView, self).get_queryset()
        # return qs.filter.conc_id
        return qs.filter(isactive=True).order_by('concession')

    def get_context_data(self, **kwargs):
        context = super(ConcstableListView, self).get_context_data(**kwargs)
        context['nav_concession'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = ConcessionTable(self.get_queryset())
        context['table'] = table
        RequestConfig(self.request, paginate={
                      'per_page': 200}).configure(table)
        return context


class WellstableView(ListView):
    model = WellGeoinfo
    # fields = ['well_id','exploration_name', 'egpc_name',
    #               'production_name','well_type','well_status','spud_date']

    form_class = wellforms.Well_Form
    context_object_name = 'wells'
    template_name = 'wells/wells_table.html'
    # ordering = ['-exploration_name']
    ordering = ['exploration_name']
    # group_required = u'operator'
    paginate_by = 200

    def get_queryset(self):
        qs = super(WellstableView, self).get_queryset()
        # return qs.filter.conc_id
        return qs.filter(concession=self.kwargs['conc_id'])

    def get_context_data(self, **kwargs):
        context = super(WellstableView, self).get_context_data(**kwargs)
        context['nav_WellGeoinfo'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = WellGeoinfoTable(self.get_queryset())
        context['table'] = table
        context['conc_id'] = self.kwargs['conc_id']
        context['conc_name'] = Concession.objects.filter(
            id=self.kwargs['conc_id']).first().concession
        RequestConfig(self.request, paginate={
                      'per_page': 200}).configure(table)
        return context


def is_member(user):  # not in  geomatics_admin
    return user.groups.filter(name='geomatics_can_delete').exists()


@login_required
@user_passes_test(is_member)  # or @user_passes_test(is_in_multiple_groups)
def delete_item(request, pk):
    obj = get_object_or_404(WellGeoinfo, well_id=pk)
    # print(obj.well_id)
    # WellGeoinfo.objects.filter(well_id=pk).delete()
    # obj.delete()
    if request.method == "POST":

        # print(" in If Object deleted" , obj.exploration_name)
        obj.delete()
        # obj.save()
        return redirect("../")
    else:
        pass
        # print("Delete Not Post",obj.exploration_name)
    # items = WellGeoinfo.objects.all()

    context = {
        'object': obj
    }

    return render(request, 'wells/delete_confirmation.html', context)


def add_to_cart(request, pk):
    app_url = request.path
    # print (app_url)
    return render_to_response(request)


def delete_from_cart(request, pk):
    pass


def selectedWellsCart(request):
    # pks = request.session['pks']
    # print("Current URL1" , request.get_full_path )
    # print("Current URL2" ,request.path)
    # print("Current URL3" ,request.build_absolute_uri)

    cart_items = request.session['cart']
    pks = cart_items.keys()

    queryset = WellGeoinfo.objects.filter(pk__in=pks)
    f = WellsFilter(request.GET, queryset=queryset)

    # if request.method == "POST":
    #     pks = request.POST.getlist("select_chkbox")
    #     request.session['pks'] = pks
    #     queryset = WellGeoinfo.objects.filter(pk__in=pks)
    #     f = WellsFilter(request.GET, queryset=queryset)
    #     print('pks',pks)
    #     print(request.session)

    #     # do something with selected_objects
    # else:
    #     print('Else No pks found')

    # return render(request, 'wells/home.html')
    table = WellGeoinfoTable(f.qs)
    table.request = request

    table.exclude = ('select_chkbox')
    # table.columns['add_to_list'].header ="Select"
    RequestConfig(request, paginate={'per_page': 35}).configure(table)

    if request.method == "POST":
        # get the redirect location
        # print("GGGGGGGGGGGGGGGGGGGG")
        redirect_to = request.POST.get('next', '')
        # print(redirect_to)
        # url_is_safe = is_safe_url(redirect_to)
        if redirect_to:  # and url_is_safe:
            return redirect(redirect_to)
        # return redirect(new_user)

    CurrentPathBeforeLeave = request.META.get('HTTP_REFERER', None) or '/'
    print("CurrentPathBeforeLeave -------------- ", CurrentPathBeforeLeave)

    return render(request, 'wells/selected_wells.html', {'table': table, 'filter': f})


def addMultiple_ToCart(request):
    # queryset = WellGeoinfo.objects.all()
    # f = WellsFilter(request.GET, queryset=queryset)
    if request.method == "POST":
        pks = request.POST.getlist("select_chkbox")
        print("iiiiiiiiiiiiiiiiii", pks)

        # cart_items = request.session['cart']
        cart2 = Cart(request)
        for i in pks:

            cart2.add(i)

        # request.session['cart'] =cart2

        # queryset = WellGeoinfo.objects.filter(pk__in=pks)
        # f = WellsFilter(request.GET, queryset=queryset)
        # print('pks',pks)
        # print(request.session)
        # # do something with selected_objects
    else:
        pass
    #     print('Else No pks found')
    # # return render(request, 'wells/home.html')
    # table = WellGeoinfoTable(f.qs)
    # RequestConfig(request, paginate={'per_page': 35}).configure(table)
    # # return render(request, 'wells/wellstable_concession_filter.html', {'conc_id':conc_id,'table': table,'filter': f})
    return redirect('selectedWellscart')


def WellsInConc_table_filter(request, conc_id):
    # queryset=WellGeoinfo.objects.select_related().all()
    queryset = WellGeoinfo.objects.filter(concession=conc_id)
    f = WellsFilter(request.GET, queryset=queryset)
    table = WellGeoinfoTable(f.qs)
    table.request = request
    print("ddf")

    # print ("request.user.group No User",request.user)

    if request.user.is_authenticated:

        if not (request.user.groups.filter(name='geomatics_can_delete').exists()):
            # print ("request.user:::::::::: ",request.user.username)
            table.exclude = ('delete')
    else:
        table.exclude = ('add_to_list', 'select_chkbox', 'delete')
    # table.exclude = ('del_from_list')

    # table.columns['add_to_list'].header ="Select"
    # table.paginate(per_page=35)
    RequestConfig(request, paginate={'per_page': 35}).configure(table)
    # cart_well_form = CartAddItemForm()

    # if request.method == "POST":
    #     pks = request.POST.getlist("select_chkbox")
    #     # selected_objects = WellGeoinfo.objects.filter(pk__in=pks)
    #     # print("POST Pks::",pks)
    #     # do something with selected_objects
    # else:
    #     pks = request.GET.getlist("select_chkbox")
    #     # selected_objects = WellGeoinfo.objects.filter(pk__in=pks)
    #     # print("GET Pks::",pks)

    return render(request, 'wells/wellstable_concession_filter.html', {'conc_id': conc_id, 'table': table, 'filter': f})


class Wellstable_filter(SingleTableMixin, FilterView):
    table_class = WellGeoinfoTable
    model = WellGeoinfo
    template_name = 'wells/wellstable_filter.html'
    filterset_class = WellsConcFilter  # WellsFilter
    paginate_by = 35

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = context['table']
        table.request = self.request

        if self.request.user.is_authenticated:

            if not (self.request.user.groups.filter(name='geomatics_can_delete').exists()):
                # print ("request.user:::::::::: ",request.user.username)
                table.exclude = ('delete')
        else:
            table.exclude = ('add_to_list', 'select_chkbox', 'delete')
        # table.exclude = ('del_from_list')
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(Wellstable_filter, self).get_context_data(**kwargs)
    #     context['nav_WellGeoinfo'] = True
    #     context['conc_id']=self.kwargs['conc_id']
    #     context['conc_name']=Concession.objects.filter(id=self.kwargs['conc_id']).first().concession
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(Wellstable_filter, self).get_context_data(**kwargs)
    #     table = self.WellGeoinfoTable()
    #     RequestConfig(self.request, paginate={'per_page': 200}).configure(table)
    #     return context


class Welllist_filter(ListView):
    model = WellGeoinfo
    template_name = 'wells/wells_filter.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = WellsFilter(
            self.request.GET, queryset=self.get_queryset())
        table = context['table']
        table.request = self.request
        # table = WellGeoinfoTable(self.get_queryset())
        # table.exclude = ('del_from_list')
        # print ("FFFFFFFFFFFFF Table Execlod ")
        return context


class WellstableListView(ListView, FilterView):
    model = WellGeoinfo
    table_class = WellGeoinfoTable
    context_object_name = 'wells'
    template_name = 'wells/wells_tablelist.html'
    filterset_class = WellGeoinfoTable
    ordering = ['exploration_name']
    paginate_by = 200

    def get_queryset(self):
        qs = super(WellstableListView, self).get_queryset()
        return qs.filter(concession=self.kwargs['conc_id']).order_by('exploration_name')

    def get_context_data(self, **kwargs):
        context = super(WellstableListView, self).get_context_data(**kwargs)
        context['nav_WellGeoinfo'] = True
        table = WellGeoinfoTable(self.get_queryset())
        table.request = self.request
        # table.exclude = ('del_from_list')
        context['table'] = table
        context['conc_id'] = self.kwargs['conc_id']
        context['conc_name'] = Concession.objects.filter(
            id=self.kwargs['conc_id']).first().concession
        RequestConfig(self.request, paginate={
                      'per_page': 200}).configure(table)
        return context


class WellUpdateView(LoginRequiredMixin, UpdateView):
    model = WellGeoinfo
    form_class = wellforms.wellDetail_form
    template_name = 'wells/well_table-crispy-class.html'
    # template_name = 'wells/wellgeoinfo_form.html'
    #
    #  'wells/well_table-crispy-class.html'

    # *******  get_object is not required with Model defined up
    # def get_object(self, form_class=None):
    #     pk_=self.kwargs.get("pk")
    #     return get_object_or_404(WellGeoinfo,pk=pk_)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        # form = self.get_form(form_class)
        # formset =  wellforms.ApprovedFormSet(instance=self.object)
        form = super(WellUpdateView, self).get_form()
        # form.can_delete = True
        # form.fields['app_id'].queryset = Approved.objects.filter(well_info=self.kwargs['pk'])

        # context = self.get_context_data(object=self.object)
        # formset3 =  context['formset3']
        # formset3.instance = self.object
        # form.fields['st'].queryset = Staked.objects.filter(well_info=self.kwargs['pk'])
        # staked_query = Staked.objects.filter(well_info=self.kwargs['pk'])
        return form

    def get_context_data(self, **kwargs):
        context = super(WellUpdateView, self).get_context_data(**kwargs)
        # formset =  wellforms.ApprovedFormSet(instance=self.object)

        # context = self.get_context_data(object=self.object)
        # cart_well_form = CartAddItemForm()

        if self.request.POST:
            # context['formset'] = wellforms.ApprovedFormSet(self.request.POST,instance=self.object)
            # context['formset2'] = formset2
            # context['formset3'] = formset3

            formset = wellforms.ApprovedFormSet(
                self.request.POST, instance=self.object)
            formset2 = wellforms.StakeoutFormSet(
                self.request.POST, instance=self.object)
            formset3 = wellforms.CheckFormSet(
                self.request.POST, instance=self.object)

            formset2.instance = self.object
            for form2 in formset2:
                form2.fields['app'].queryset = Approved.objects.filter(
                    well_info=self.object.pk)

            formset3.instance = self.object
            for form3 in formset3:
                form3.fields['st'].queryset = Staked.objects.filter(
                    well_info=self.object.pk)

        else:
            # context['formset'] = wellforms.ApprovedFormSet(instance=self.object)
            formset = wellforms.ApprovedFormSet(instance=self.object)
            formset2 = wellforms.StakeoutFormSet(instance=self.object)
            formset3 = wellforms.CheckFormSet(instance=self.object)

            newStakeForm = wellforms.StakeoutForm()

            formset2.instance = self.object
            for form2 in formset2:
                form2.fields['app'].queryset = Approved.objects.filter(
                    well_info=self.object.pk)

            formset3.instance = self.object
            for form3 in formset3:
                form3.fields['st'].queryset = Staked.objects.filter(
                    well_info=self.object.pk)

        context['formset'] = formset
        context['formset2'] = formset2
        context['formset3'] = formset3
        # context['cart_well_form'] = cart_well_form  # 'cart_well_form': cart_well_form

        return context

    def form_valid(self, form):

        if self.request.method == 'POST':
            self.object = form.save()
            self.object = form.save(commit=False)

            context = self.get_context_data(object=self.object)

            formset = context['formset']
            formset2 = context['formset2']
            formset3 = context['formset3']
            formset.instance = self.object
            formset2.instance = self.object
            formset3.instance = self.object

            time.sleep(3)

            if self.request.POST.get('concession'):
                if form.is_valid():
                    print("Valid Main Form 0 ")
                if formset.is_valid():
                    print("Valid Formset 1 Form ")

                else:
                    print("InValid Formset 1 Form ")
                    # print (formset)
                if formset2.is_valid():
                    print("Valid Formset2 2 Form ")
                else:
                    print("InValid Formset2 2 Form ")
                if formset3.is_valid():
                    print("Valid Formset3 3 Form ")
                else:
                    print("InValid Formset3 3 ")

                if form.is_valid() and formset.is_valid() and formset2.is_valid() and formset3.is_valid():
                    self.object.save()
                    form.save()
                    # formset = wellforms.ApprovedFormSet(self.request.POST)

                    formset3.save()
                    formset2.save()
                    formset.save()

                else:
                    print("Invalid form HHHHHHHHHHHHH")
            else:
                print("Invalid field")
        return super().form_valid(form)

    # , approved_formset,staked_formset,checked_formset):
    def form_invalid(self, form):
        # self.object = form.save(commit=False)
        print('FormInvalid5555')
        context = self.get_context_data(object=self.object)

        approved_formset = context['formset']
        staked_formset = context['formset2']
        checked_formset = context['formset3']

        """
        If either of the forms are invalid
        Re-render the page with data-filled forms and errors
        """
        return self.render_to_response(self.get_context_data(form=form, formset=approved_formset, formset2=staked_formset, formset3=checked_formset))


class AddWellView(CreateView):
    model = WellGeoinfo
    form_class = wellforms.Well_Form
    template_name = 'wells/well_form.html'
    success_url = '/wells/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add New Well"
        return context


def home(request):
    context = {
        'concessions': Concession.objects.all()
    }

    # request.session['pks']=()
    cart = request.session[settings.CART_SESSION_ID] = {}

    print(request.user)
    print(request.META['REMOTE_ADDR'])
    # print(request.META['REMOTE_USER'])

    return render(request, 'wells/home.html', context)

    context = {
        'concessions': Concession.objects.all()
    }

    return render(request, 'wells/selectconc.html', context)


def about(request):
    return render(request, 'wells/about.html', {'title': 'About'})


class CreateWell(LoginRequiredMixin, CreateView):
    model = WellGeoinfo
    form_class = wellforms.wellcreate_form

    context_object_name = 'well'
    template_name = 'wells/well_create_form.html'

    # def get_initial(self):
    #     return { 'concession': self.kwargs['conc_id']}

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(CreateWell, self).get_form()

        return form

    def form_invalid(self, form):
        """
        If either of the forms are invalid
        Re-render the page with data-filled forms and errors
        """
        return self.render_to_response(self.get_context_data(form=form))


class CreateWell_inConc(CreateView):
    model = WellGeoinfo
    form_class = wellforms.wellcreate_form

    context_object_name = 'well'
    template_name = 'wells/well_table-crispy-class.html'

    def get_initial(self):
        return {'concession': self.kwargs['conc_id']}

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(CreateWell_inConc, self).get_form()

        return form

    def form_invalid(self, form):
        """
        If either of the forms are invalid
        Re-render the page with data-filled forms and errors
        """
        return self.render_to_response(self.get_context_data(form=form))


def coordconv(request):

    if request.method == "POST":
        form = wellforms.coord_conv_form(request.POST)

        if form.is_valid():
            # print ("In View Form is valid")

            xlong_to = form.cleaned_data['outputX']
            ylat_to = form.cleaned_data['outputY']

            lat_to = form.cleaned_data['outputLat']
            long_to = form.cleaned_data['outputLong']

            return render(request, 'wells/coordconv.html', {'form': form, 'x': xlong_to, 'y': ylat_to, 'Lat': lat_to, 'Long': long_to})
            # return HttpResponseRedirect(reverse('coordconv'))
        else:
            print("InView Form not valid")
    else:
        form = wellforms.coord_conv_form()
        return render(request, 'wells/coordconv.html', {'form': form})
