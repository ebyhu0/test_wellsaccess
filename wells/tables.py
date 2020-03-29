from django.utils.html import format_html
from django.template import RequestContext


import django_tables2 as tables
from django_tables2 import SingleTableView
from django.urls import reverse

from importlib import import_module
from django.conf import settings

import itertools
from django_tables2.utils import A
from .models import Concession,WellGeoinfo,Approved
from . import bap_lib
from wells import views


class ConcessionTable(tables.Table):
  concession = tables.LinkColumn('WellsInConc_table_filter', args=[A('pk')])
  operator = tables.LinkColumn('WellsInConc_table_filter', args=[A('pk')])
  isactive = tables.LinkColumn('WellsInConc_table_filter', args=[A('pk')])
  
 
  class Meta:
        model = Concession
        fields = ('id','concession','concessiontype',
                  'isactive','area_km2',
                  'operator')
                  
        attrs = {"class": "table-striped table-bordered",'width':'100%'}
        empty_text = "There are no concession matching the search criteria..."
        # row_attrs = {
        #     'conc-id': lambda record: record.pk
        # }

class WgsColumn(tables.Column):
    
    def render(self, record):
        return record.exploration_name

# <a href="{% url 'delete_item' record.well_id %}">Delete</a>
TEMPLATE = '''
<a  
    class="btn btn-danger pull-right" 
    href="{% url 'delete_item' record.well_id  %}"> Delete
</a>
'''
TEMPLATE_CART_ADD = '''
<a  
    class="btn btn-info pull-right" 
    href="{% url "cart:cart_add" record.well_id %}"> Add
</a>
'''

TEMPLATE_CART_DEL = '''
<a  
    class="btn btn-info pull-right" 
    href="{% url "cart:cart_remove" record.well_id %}"> Del
</a>
'''

TEMPLATE_disabledButton = '''
<a  
    class="btn btn-info pull-outline" 
    href="#"> Selected
</a>
'''
class CheckBoxColumnWithName(tables.CheckBoxColumn):
    
    @property
    def header(self):
        return self.verbose_name

class WellGeoinfoTable(tables.Table):
        # select_chkbox = tables.CheckBoxColumn( accessor="pk")
        # select_chkbox = tables.TemplateColumn('<input type="checkbox" value="{{ record.pk }}" />', verbose_name="Select")
        # select_chkbox = CheckBoxColumnWithName(verbose_name="Select", accessor="pk", attrs = { "th__input":{"onclick": "toggle(this)"}},orderable=False)
        select_chkbox= tables.CheckBoxColumn(accessor="pk", attrs = {"th__input":{"onclick": "toggle(this)"},"td__input":{"onclick": "countbox(this)"}},
                                        orderable=False)
                                    
        SN = tables.Column(empty_values=(),orderable=False)

        PSD = tables.Column(empty_values=())
        prov_name = tables.Column(empty_values=())

        exploration_name = tables.LinkColumn('update-well-view', args=[A('pk')])
        
        Easting = tables.Column(empty_values=())
        Northing = tables.Column(empty_values=())
        Latitude = tables.Column(empty_values=())
        Longitude = tables.Column(empty_values=())

        Latitude_WGS84 = tables.Column(empty_values=())
        Longitude_WGS84 = tables.Column(empty_values=())

 
        delete = tables.TemplateColumn(TEMPLATE,orderable=False)
        
        add_to_list = tables.TemplateColumn(TEMPLATE_CART_ADD,verbose_name="Select",orderable=False)
        # del_from_list = tables.TemplateColumn(TEMPLATE_CART_DEL,verbose_name="Select",orderable=False)


        # delete = tables.LinkColumn('delete_item', args=[A('pk')], attrs={
        #     'a': {'class': 'btn btn-small btn-dark'}
        #     })


        def render_add_to_list(self,record):
            # SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
            # s=SessionStore()
            # # print ('hhhhhhhhhhhhhhhhhhh',s.cart)
            # cart_items = s['cart']
            # print ("HHHHHHHHHHHHH In Render")
            if self.request.user.is_authenticated:
                # print ("OOOOOOOOOOOOOOOO")
                cart_items = self.request.session['cart']
                pks = cart_items.keys()
                # print ("HHHHHHHHHHHHH", pks)
            
                if str(record.pk) in pks:
                    # print("record.pk11111: " , record.pk)
                    url2 = reverse('cart:cart_remove', args=(record.well_id,))
                    url2 = reverse('cart:cart_remove', args=[record.well_id])
                    url2 = reverse('cart:cart_remove',kwargs={'well_id': record.well_id})
                    #         '%s:%s_%s_change' % (
                    #             self.admin_site.name,
                    #             obj._meta.app_label,
                    #             obj._meta.object_name.lower(),
                    #         ),
                    #         args=(obj.pk,)
                    #     )
                    str4 = '<a style="width:85px" class="btn btn-outline-info" href="{}"> Deselect </a>'
                    # return  format_html( '<a class="btn btn-info pull-outline" href="#"> Add </a>' , record)   
                    
                    return  format_html(str4,url2)   


                    # return format_html('<a class="btn btn-outline-info" href="#"> Selected </a>', record)
                else:
                    # print("record.pk2222: " , record.pk)
                    # url2 = reverse('selectedWellscart')
                    url2 = reverse('cart:cart_add', args=(record.well_id,))
                    url2 = reverse('cart:cart_add', args=[record.well_id])
                    url2 = reverse('cart:cart_add',kwargs={'well_id': record.well_id})
                    #         '%s:%s_%s_change' % (
                    #             self.admin_site.name,
                    #             obj._meta.app_label,
                    #             obj._meta.object_name.lower(),
                    #         ),
                    #         args=(obj.pk,)
                    #     )
                    str4 = '<a style="width:85px" class="btn btn-info pull-right" href="{}"> Select </a>'
                    # return  format_html( '<a class="btn btn-info pull-outline" href="#"> Add </a>' , record)   
                    
                    return  format_html(str4,url2)
                return ("UUUU")   

        def render_PSD(self,record):
                if record.app_id:
                    return record.app_id.projection.psd_name
                else:
                    return None
                

        def render_prov_name(self,record):
                if record.app_id:
                    return record.app_id.app_name
                else:
                    return None

        def __init__(self, *args, **kwargs):
            super(WellGeoinfoTable, self).__init__(*args, **kwargs)
            self.counter = itertools.count(1)
            # self.cells = CellAccessor(self)

 
        def render_SN(self,record):
            
            # print("DDDDDDDD")

                Input_eastX= record.east_red
                Input_northY= record.north_red
            
                if record.app_id:
                    psd_From =  22992 # RedBelt
                    psd_To = record.app_id.projection.epsg  #4326 # WGS84

                    # if record.app_id.projection.epsg != 22992:
                    record.Easting,record.Northing,zcart_to, record.Longitude,record.Latitude,zcart2_to = bap_lib.coord_conv(psd_From,psd_To,Input_eastX,Input_northY)
                    # else:
                        # record.Easting= format(round(record.east_red,2),'.2f')
                        # record.Northing= format(round(record.north_red,2),'.2f')
                        # record.Longitude= bap_lib.ddmmss_to_dms(str(record.long_red)) + " E"
                        # record.Latitude= bap_lib.ddmmss_to_dms(str(record.lat_red)) + " N"


                    psd_To = 4326  #4326 # WGS84
                    x2,y2,z2,record.Longitude_WGS84,record.Latitude_WGS84,z2 = bap_lib.coord_conv(psd_From,psd_To,Input_eastX,Input_northY)
                    # print(self.page.number)
                    # print(self.paginator.num_pages)
                    # print(self.paginator.per_page)

                pg = getattr(self, 'paginator', None)
                if pg:
                    v=next(self.counter)
                    return v + self.paginator.per_page * (self.page.number-1) #'Row %d' % next(self.counter)
                else:
                    return next(self.counter)
                # return next(self.counter)
    
        class Meta:
            model = WellGeoinfo
            fields = ('select_chkbox','add_to_list','SN','well_id','prov_name','exploration_name','uwi_operation_shell','wims_name_shell','production_name','sap_functional_location','egpc_name','owner_original', 
                        'well_type','well_status',
                        'Latitude','Longitude','Easting','Northing','elevation','PSD',
                        'Latitude_WGS84','Longitude_WGS84',
                        'delete',
                        )
                        
            attrs = {"class": "table-striped table-bordered",'width':'100%'}
            empty_text = "There are no concession matching the search criteria..."

class ApprovedTable(tables.Table):
    # prov_name = tables.LinkColumn('edit-well', args=[A('pk')])

  
  class Meta:
        model = WellGeoinfo
        fields = ('app_id','prov_name','app_name', 'app_xline', 'app_xline',
        'app_east','app_north','app_elev','app_date','app_type','projection',
        'prov_seismic_vintage','prov_well_type','prov_from','prov_interpreter_name')
                  
        attrs = {"class": "table-striped table-bordered",'width':'200%'}
        empty_text = "There are no concession matching the search criteria..."


  
class WellGeoinfoList(SingleTableView):
    model = WellGeoinfo
    table_class = WellGeoinfoTable