from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.forms import ModelForm

from .models import Concession, WellGeoinfo
from .tables import ConcessionTable,WellGeoinfoTable


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class Well_Form(ModelForm):
    # the_id = forms.IntegerField(widget=forms.HiddenInput)

    # def __init__(self, *args, **kwargs):
    #     super(Well_Form, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         # self.fields['wellname_id'].widget.attrs['readonly'] = True
    #         # wellname_id = forms.IntegerField(min_value = 1, required=True)
    #         # self.fields['wellname_id'].widget.attrs= 'visible'
    #         self.fields["the_id"].initial = instance.well_id
    #         self.fields['the_id'].widget.attrs['readonly'] = True

    class Meta:
        model = WellGeoinfo
        fields = ['well_id','concession', 'exploration_name','egpc_name','east_red','north_red','elevation','well_type','well_status']
        # labels = { 'prop_name': _('prop_name'), }
        # help_texts = { 'prop_name': _('prop_name (default 3).'), }

def WellDetail_pp(request, pk):
    well = get_object_or_404(WellGeoinfo, pk=pk)
    form = Well_Form(request.POST or None, instance=well)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('edit-well', pk=well.pk)

    return render(request, 'wells/well_form.html',{'form':form,'title':"Edit Well Form"})      

class AddWellView(CreateView):
    # class AddWellView(LoginRequiredMixin, CreateView):
    # model = WellGeoinfo
    # fields = ['concession', 'well_id', 'proposedname', 'exploration_name']
    form_class = Well_Form
    template_name = 'wells/well_form.html'
    success_url = '/wells/'
   

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['title'] = "Add New Well"
        return context

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class WellstableView(ListView):
    model = WellGeoinfo
    

    fields = ['well_id','exploration_name', 'egpc_name',
                  'production_name','well_type','well_status','spud_date']
    context_object_name = 'wells'
    template_name = 'wells/wells_table.html'
    # ordering = ['-exploration_name']
    ordering = ['exploration_name']
    # group_required = u'operator'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(WellstableView, self).get_context_data(**kwargs)
        context['nav_WellGeoinfo'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = WellGeoinfoTable(WellGeoinfo.objects.filter(concession=self.kwargs['conc_id']))
        # RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

    # def get_queryset(self):
    #     # conc_id = self.request.GET.get('conc_id') 
    #     qs = super(ConcListView, self).get_queryset()
    #     # return qs.filter.conc_id
    #     return qs.filter(id=self.kwargs['conc_id'])
        
class ConctableView(ListView):
    model = Concession
    fields = ['concession', 'area_km2',
              'concessiontype', 'operator', 'isactive']
    context_object_name = 'concs'
    template_name = 'wells/conc_table.html'
    # ordering = ['-exploration_name']
    ordering = ['concession']
    # group_required = u'operator'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ConctableView, self).get_context_data(**kwargs)
        context['nav_concession'] = True
        # table = ConcessionTable(Concession.objects.filter(self.kwargs['concession']).order_by('-pk'))
        table = ConcessionTable(Concession.objects.filter(isactive=True))
        # RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

class ConcessionModelForm(ModelForm):

    class Meta:
        model = Concession
        readonly_fields = ['id', ]
        fields = ['concession', 'area_km2',
                  'concessiontype', 'operator', 'isactive']

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



class WellListView(ListView):
    model = WellGeoinfo
    fields = ['concession', 'well_id', 'proposedname', 'exploration_name']
    context_object_name = 'wells'
    template_name = 'wells/well_list.html'
    # ordering = ['-exploration_name']
    ordering = ['-well_id']
    paginate_by = 10

class ConcListView(ListView):
    # conc_id=self.kwargs['conc_id']
    
    # model = Concession.objects.filter(id=conc_id)
    model = Concession
    fields = ['concession', 'area_km2',
              'concessiontype', 'operator', 'isactive']
    context_object_name = 'concs'
    template_name = 'wells/conc_list.html'
    # ordering = ['-exploration_name']
    ordering = ['concession']
    paginate_by = 10
    
    # def get(self, *args, **kwargs):
    #     print('Processing GET request')
    #     resp = super().get(*args, **kwargs)
    #     print('Finished processing GET request')
    #     return resp
    

def ConcessionWellsList(request, conc_id):

    concession = Concession.objects.get(pk=conc_id)

    WellsFormset = inlineformset_factory(Concession, WellGeoinfo, fields=(
        'well_id', 'exploration_name', 'concession'), extra=1, can_delete=False)
    # WellsFormset=inlineformset_factory(Concession,WellGeoinfo,form=wellForm )

    if request.method == 'POST':
        formset = WellsFormset(request.POST, instance=concession)
        if formset.is_valid():
            formset.save()

            return redirect('wells/concwell_list.html', concession_id=concession.id)

    formset = WellsFormset(instance=concession)

    return render(request, 'wells/concwell_list.html', {'formset': formset})


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

class ConcessionDetailView(DetailView):
    model = Concession

# class WellListView(LoginRequiredMixin, ListView):

# class wellForm(ModelForm):
#     # def __init__(self, *args, **kwargs):
#     #     super(wellForm, self).__init__(*args, **kwargs)
#     #     instance = getattr(self, 'instance', None)
#     #     if instance and instance.pk:
#     #         # self.fields['pk'].widget.attrs['readonly'] = True
#     #         self.fields['concession'].widget.attrs['readonly'] = True

#     class Meta:
#         model = WellGeoinfo
#         readonly_fields = ['well_id']
#         list_display = ['well_id','exploration_name',]
#         fields = ['well_id','exploration_name','concession',]


# class WellDetailView(DetailView):
#     model = WellGeoinfo
#     fields = ['well_id','exploration_name', 'egpc_name',
#                   'production_name','well_type','well_status','spud_date']
#     form_class = Well_Form
#     template_name = 'wells/well_form.html'
#     context_object_name = 'well'

#     @property
#     def title (self):
#         return "Add New Well"
