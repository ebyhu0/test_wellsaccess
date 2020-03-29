from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.db.models import F
from osgeo.osr import SpatialReference, CoordinateTransformation

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_tables2 import RequestConfig
from django_filters.views import FilterView

from django.db import transaction
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from . import forms as wellforms
from django.forms import ModelForm

from .models import Concession, WellGeoinfo,Approved,Provisional,Psd
from .tables import ConcessionTable,WellGeoinfoTable,ApprovedTable


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

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
            return qs.filter(isactive=True)


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
    paginate_by = 10

    def get_queryset(self):
            qs = super(ConcstableListView, self).get_queryset()
            # return qs.filter.conc_id
            return qs.filter(isactive=True)


    def get_context_data(self, **kwargs):
        context = super(ConcstableListView, self).get_context_data(**kwargs)
        context['nav_concession'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = ConcessionTable(self.get_queryset())
        context['table'] = table
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
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
    paginate_by = 10

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
        context['conc_id']=self.kwargs['conc_id']
        context['conc_name']=Concession.objects.filter(id=self.kwargs['conc_id']).first().concession
        # RequestConfig(self.request, paginate={'per_page': 20}).configure(table)
        return context

class WellstableListView(ListView, FilterView):
    model = WellGeoinfo
    # fields = ['well_id','exploration_name', 'egpc_name',
    #               'production_name','well_type','well_status','spud_date']
    
    form_class = wellforms.Well_Form
    context_object_name = 'wells'
    template_name = 'wells/wells_tablelist.html'
    filterset_class = WellGeoinfoTable
    # ordering = ['-exploration_name']
    ordering = ['exploration_name']
    # group_required = u'operator'
    paginate_by = 10

    def get_queryset(self):
        qs = super(WellstableListView, self).get_queryset()
        # return qs.filter.conc_id
        return qs.filter(concession=self.kwargs['conc_id'])

    def get_context_data(self, **kwargs):
        context = super(WellstableListView, self).get_context_data(**kwargs)
        context['nav_WellGeoinfo'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = WellGeoinfoTable(self.get_queryset())
        context['table'] = table
        context['conc_id']=self.kwargs['conc_id']
        context['conc_name']=Concession.objects.filter(id=self.kwargs['conc_id']).first().concession
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        return context

# def just_a_fun(request, **kwargs):
#     context = kwargs if kwargs else {"method": "just a function"}
#     return HttpResponse('method = %(method)s' % context)
def coord_conv(epsg_from,epsg_to,cord_xlong,cord_ylat):
    # 
        if epsg_from and epsg_to :

            epsgfrom = SpatialReference()
            epsgfrom.ImportFromEPSG(epsg_from)

            if epsg_from!=4326:
                epsgfrom.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)

            epsgto = SpatialReference()
            epsgto.ImportFromEPSG(epsg_to)

            if epsg_to!=4326:
                epsgto.SetTOWGS84(-121.8,98.1,-10.7,0,0,0.554,-0.2263)
        # ----------------------------
        FromTo_psd = CoordinateTransformation(epsgfrom, epsgto)
        xlong,ylat,zcart = FromTo_psd.TransformPoint(cord_xlong, cord_ylat)

        # print(xlong,ylat,zcart)
        return (xlong,ylat,zcart)

def SetFinal(request,app_id):
    # Approved.objects.filter(pk=pk).update(views=F('views')+1)
    
    finalapp=Approved.objects.filter(app_id=app_id).first()
    wellInApp=finalapp.well_info
    provid=finalapp.prop.pk

    finalprov=Provisional.objects.filter(pk=provid).first()
    allapp=Approved.objects.filter(well_info=wellInApp.pk)
    allprov=Provisional.objects.filter(well_info=wellInApp.pk)
    wellinfoRow=WellGeoinfo.objects.filter(pk=wellInApp.pk).first()

    allapp.update(app_type='Option')
    allprov.update(prov_type='Option')

    finalapp.app_type='Final'
    finalprov.prov_type='Final'
    # finalapp.save()
    finalprov.prov_east=finalapp.app_east
    finalprov.prov_north=finalapp.app_north
    
    wellinfoRow.app_id=finalapp
    epsg_From=finalapp.projection.epsg
    epsg_To=22992 # RedBelt
    
    East,North,zcart1=coord_conv(epsg_From,epsg_To,finalapp.app_east,finalapp.app_north)

    epsg_To=4229 # Egy1907
    Longitude,Latitude,zcart2=coord_conv(epsg_From,epsg_To,finalapp.app_east,finalapp.app_north)
    
    # print('FFFFFFFFFFFSSSSSSSSSSSSSSSS')
    # print (epsg_From,East,North,zcart1)
    # print (epsg_From,Longitude,Latitude,zcart2)
    
    wellinfoRow.lat_red=Latitude
    wellinfoRow.long_red=Longitude
    wellinfoRow.lat_EG_dd=Latitude
    wellinfoRow.long_EG_dd=Longitude
    wellinfoRow.east_red=East
    wellinfoRow.north_red=North
    wellinfoRow.elevation=finalapp.app_elev
    
    finalapp.save()
    finalprov.save()
    wellinfoRow.save()

    return HttpResponseRedirect(reverse('update-well-view', kwargs={'pk':str(wellInApp.pk)}))

class WellUpdateView(UpdateView):
    model = WellGeoinfo
    form_class = wellforms.wellDetail_form
    template_name = 'wells/well_table-crispy-class.html'

   

    #*******  get_object is not required with Model defined up
    # def get_object(self, form_class=None):
    #     pk_=self.kwargs.get("pk")
    #     return get_object_or_404(WellGeoinfo,pk=pk_)


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        # form = self.get_form(form_class)
        # formset =  wellforms.ApprovedFormSet(instance=self.object)
        form = super(WellUpdateView, self).get_form()
        # form.fields['app_id'].queryset = Approved.objects.filter(well_info=self.kwargs['pk'])
        return form

    def get_context_data(self, **kwargs):
        context = super(WellUpdateView, self).get_context_data(**kwargs)
        # formset =  wellforms.ApprovedFormSet(instance=self.object)
        if self.request.POST:
            context['formset'] = wellforms.ApprovedFormSet(self.request.POST,instance=self.object)
        else:
            context['formset'] = wellforms.ApprovedFormSet(instance=self.object)
        return context


    def form_valid(self,form):
        # if request.method=='POST' and 'btnform1' in request.POST:
        #     do something...
        # if request.method=='POST' and 'btnform2' in request.POST:
        #     do something...

        if self.request.method=='POST':
            self.object = form.save()
            self.object = form.save(commit=False)
            context = self.get_context_data(object=self.object)
            formset =  context['formset']
            if form.is_valid() and formset.is_valid():
                # formset = wellforms.ApprovedFormSet(self.request.POST)
                formset.instance = self.object
                formset.save()
                self.object.save()
                form.save()
        # return HttpResponseRedirect( self.object.get_absolute_url())
     
        return super().form_valid(form)



class WellDetailView(DetailView):
    # model = WellGeoinfo
    form_class = wellforms.wellDetail_form
    context_object_name = 'well'
    template_name = 'wells/well_table-crispy-class.html'
    # success_url=reverse_lazy('wells:tablelist-concs')

    pk_url_kwarg = 'pk'
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WellDetailView, self).get_form()
        form.fields['app_id'].queryset = Approved.objects.filter(well_info=self.kwargs['pk'])
        form.fields['lat_red'].widget.attrs['disabled'] = 'disabled'
        form.fields['long_red'].widget.attrs['disabled'] = 'disabled'
        form.fields['east_red'].widget.attrs['disabled'] = 'disabled'
        form.fields['north_red'].widget.attrs['disabled'] = 'disabled'
        form.fields['elevation'].widget.attrs['disabled'] = 'disabled'
    
        return form

    def get(self, request, *args, **kwargs):
        """
        instantiates the form and inline formset
        """
        # self.object = self.get_object()
        pk_=self.kwargs.get("pk")
        self.object=get_object_or_404(WellGeoinfo,pk=pk_)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        approved_formset =  wellforms.ApprovedFormSet(instance=self.object)
        
        return self.render_to_response(self.get_context_data(
            form=form,
            formset=approved_formset,
        ))


    def post(self, request, *args, **kwargs):
        """
        instantiates the form with its inline formsets
        with the passed POST data and validates
        """
        # self.object = self.get_object()
        pk_=self.kwargs.get("pk")
        self.object=get_object_or_404(WellGeoinfo,pk=pk_)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        approved_formset =  wellforms.ApprovedFormSet(self.request.POST, instance=self.object)

        if form.is_valid() and approved_formset.is_valid():
            return self.form_valid(form, approved_formset)
        else:
            return self.form_invalid(form, approved_formset)

    def form_valid(self, form, approved_formset):
        """
        If both forms are valid then create Job with skills and redirect
        """
        self.object = form.save(commit=False)

        # self.object.user = self.request.user
        self.object.save()
        approved_formset.instance = self.object
        approved_formset.save()
        # return HttpResponseRedirect( self.object.get_absolute_url())
        return  self.render_to_response(self.get_context_data(form=form, formset=approved_formset))
        # return reverse('author-detail', kwargs={'pk': self.pk})
        # return reverse_lazy('wells:tablelist-concs')
       
        # return super().form_valid(form)
        

    def form_invalid(self, form, approved_formset):
        """
        If either of the forms are invalid
        Re-render the page with data-filled forms and errors
        """
        return self.render_to_response(self.get_context_data(form=form, formset=approved_formset))
        


class WellDetailViewOld(UpdateView):
    model = WellGeoinfo
    form_class = wellforms.Well_Form2
    context_object_name = 'well'
    template_name = 'wells/well_table-crispy-class.html'
    pk_url_kwarg = 'pk'
    


    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(WellDetailViewOld, self).get_form()
        form.fields['app_id'].queryset = Approved.objects.filter(well_info=self.kwargs['pk'])
        return form

    def get_context_data(self, **kwargs):
        context = super(WellDetailViewOld, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = wellforms.ApprovedFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = wellforms.ApprovedFormSet( instance=self.object)
        # RequestConfig(self.request, paginate={'per_page': 30}).configure(dataset)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        # form = context['ingredient_form']
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            # ingredient_form.instance = self.object
            formset.save()
            # form.instance = self.object
            form.save()
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

def WellDetail_pp(request, pk):
    # well=WellGeoinfo.objects.filter(pk=pk).first()
    well = get_object_or_404(WellGeoinfo, pk=pk)
    # form = wellforms.Well_Form(well,request.POST or None, instance=well)
    form = wellforms.Well_Form(well,request.POST or None,  instance=well)
    # AppProvFormset = inlineformset_factory(WellGeoinfo,Approved, fields=(
    # 'app_id','prov_name','app_name', 'app_xline', 'app_xline',
    # 'app_east','app_north','app_elev','app_date','app_type',
    # 'projection','prov_seismic_vintage','prov_well_type'), extra=1, can_delete=False)
    
    # form.fields["app_id"].queryset = Approved.objects.filter(well_info=pk)
    if request.method == 'POST':
        formset = wellforms.ApprovedFormSet(request.POST, instance=well)

        if formset.is_valid() and form.is_valid():
            formset.save()
            form.save()
            return redirect('edit-well', pk=well.pk)
    formset = wellforms.ApprovedFormSet(instance=well)

    # table = ApprovedTable(Approved.objects.filter(well_info=pk))
    # RequestConfig(request, paginate={'per_page': 30}).configure(table)

    return render(request, 'wells/well_table-crispy.html',{'form':form,'formset':formset,'title':"Edit Well Form"})      
    # return render(request, 'wells/well_table-crispy.html',{'form':form,'formset':formset,'table':table,'title':"Edit Well Form"})      
    # return render(request, 'wells/well_form.html',{'form':form,'formset':formset,'table':table,'title':"Edit Well Form"})      

def AddWellInConc_pp(request, conc_id):
    concobj=Concession.objects.filter(id=conc_id).first()
    well = WellGeoinfo.objects.create(concession=concobj)
    # well = get_object_or_404(WellGeoinfo, pk=pk)
    form = wellforms.Well_Form(request.POST or None, instance=well)
    AppProvFormset = inlineformset_factory(WellGeoinfo,Approved, fields=(
    'app_id','prov_name','app_name', 'app_xline', 'app_xline','app_east','app_north','app_elev','app_date','app_type','projection','prov_seismic_vintage','prov_well_type'), extra=1, can_delete=False)
    

    if request.method == 'POST':
        formset = AppProvFormset(request.POST, instance=well)

        if formset.is_valid() and form.is_valid():
            formset.save()
            form.save()
            return redirect('edit-well', pk=well.pk)
    formset = AppProvFormset(instance=well)

    return render(request, 'wells/well_table-crispy.html',{'form':form,'formset':formset,'title':"Edit Well Form"})      

class CreateWell(CreateView):
    model = WellGeoinfo
    form_class = wellforms.wellcreate_form
    # queryset=WellGeoinfo.objects.all()
    
    context_object_name = 'well'
    template_name = 'wells/well_table-crispy-class.html'
    # success_url=reverse_lazy('bx-home')

    # pk_url_kwarg = 'pk'
    
    def get_initial(self):
        return { 'concession': self.kwargs['conc_id']}
        
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(CreateWell, self).get_form()
        # del form.fields['app_id']
        # form.fields['app_id'].queryset = Approved.objects.filter(well_info=0)
        # form.fields['app_id'].widget = HiddenInput()
        # form.fields['well_status'].widget.attrs['disabled'] = 'disabled'
        

        return form

  
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)
    #     # self.object = form.save(commit=False)
        # self.object.save()
        # print("form valid")

        # return HttpResponseRedirect( self.object.get_absolute_url())
        
        # return  self.render_to_response(self.get_context_data(form=form))
        # return reverse('edit-well-view',kwargs={'pk':self.object.well_id})

        # return reverse('edit-well-view',kwargs={'pk':0})

        # return reverse('author-detail', kwargs={'pk': self.pk})
        # return reverse_lazy('wells:tablelist-concs')
       
        # return super().form_valid(form)
        
    # def get_success_url(self):
    #     # return reverse('edit-well-view',kwargs={'pk':self.kwargs['wellid']})
    #     pass
 

    def form_invalid(self, form):
        """
        If either of the forms are invalid
        Re-render the page with data-filled forms and errors
        """
        return self.render_to_response(self.get_context_data(form=form))
        

 
    # def post(self, request, *args, **kwargs):
    #     """
    #     instantiates the form with its inline formsets
    #     with the passed POST data and validates
    #     """
    #     form=wellforms.Well_Form2(request.POST or None)

    #     # self.object = self.get_object()
    #     # form_class = self.get_form_class()
    #     # form = self.get_form(form_class)
        
    #     # approved_formset =  wellforms.ApprovedFormSet(self.request.POST, instance=self.object)

    #     if form.is_valid() :
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)


class CreateWellOld( CreateView):
    form_class = wellforms.Well_Form2
    template_name = 'wells/well_table-crispy.html'
    # success_url='tablelist-wells'

    def get_initial(self):
        return { 'concession': self.kwargs['conc_id']}

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(CreateWell, self).get_form()
        form.fields['app_id'].queryset = Approved.objects.filter(well_info=self.kwargs['pk'])
        return form

    def get_context_data(self, **kwargs):
        data = super(CreateWell, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = wellforms.ApprovedFormSet(self.request.POST)
        else:
            data['formset'] = wellforms.ApprovedFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        # with transaction.commit_on_success():
        #     form.instance.created_by = self.request.user
        #     form.instance.updated_by = self.request.user
        
        if formset.is_valid() and form.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

        return super(CreateWell, self).form_valid(form)

    def get_success_url(self):
        return reverse('tablelist-wells',kwargs={'conc_id':self.kwargs['conc_id']})
        

# class AddWellInConcView(CreateView):
#     model=WellGeoinfo
#     form_class = wellforms.Well_Form
#     template_name = 'wells/well_form.html'
#     success_url = '/wells/'
   
#     form = wellforms.Well_Form(request.POST or None, instance=well)
#     AppProvFormset = inlineformset_factory(WellGeoinfo,Approved, fields=(
#     'app_id','prov_name','app_name', 'app_xline', 'app_xline','app_east','app_north','app_elev','app_date','app_type','projection','prov_seismic_vintage','prov_well_type'), extra=1, can_delete=False)
 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Add New Well"
#         context['conc_id']=self.kwargs['conc_id']
#         qs = super(Approved, self).get_queryset()
#         # return qs.filter.conc_id
#         qs.filter(well_info=self.kwargs['conc_id'])
#         table = ApprovedTable(sq.get_queryset())
#         context['table'] = table
#         RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
#         return context

#     def get_initial(self):
#         return { 'concession': self.kwargs['conc_id']}

# class AddWellInConcView(CreateView):
#     model=WellGeoinfo
#     form_class = wellforms.Well_Form
#     template_name = 'wells/well_form.html'
#     success_url = '/wells/'
   

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Add New Well"
#         context['conc_id']=self.kwargs['conc_id']
#         qs = super(Approved, self).get_queryset()
#         # return qs.filter.conc_id
#         qs.filter(well_info=self.kwargs['conc_id'])
#         table = ApprovedTable(sq.get_queryset())
#         context['table'] = table
#         RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
#         return context

#     def get_initial(self):
#         return { 'concession': self.kwargs['conc_id']}

class AddWellView(CreateView):
    model=WellGeoinfo
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
