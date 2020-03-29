# ----------ArcPy--------------
# import arcpy
# import pandas

# # connect to GIS
# from arcgis.gis import GIS
# from arcgis.features import FeatureLayerCollection
# # from arcgis.features import features
# # import pandas as pd
# from arcgis.features import GeoAccessor, GeoSeriesAccessor
# from IPython.display import display
# --------------------------

import datetime
from django.forms import DateTimeInput


from . import bap_lib

import math 

from osgeo.osr import SpatialReference, CoordinateTransformation
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import inlineformset_factory, modelformset_factory


from django.forms import ModelForm
from django.forms import widgets

from .models import WellGeoinfo,Concession,Approved,Staked,Checked,Psd

from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column,HTML,Div

class ConcessionModelForm(ModelForm):
    
    class Meta:
        model = Concession
        readonly_fields = ['id', ]
        fields = ['concession', 'area_km2',
                  'concessiontype', 'operator', 'isactive']


class wellDetail_formlayout_Old(ModelForm):
        def __init__(self, *args, **kwargs):

            super(wellDetail_formlayout_Old, self).__init__(*args, **kwargs)
            # instance = getattr(self, 'instance', None)
            self.helper = FormHelper()
            self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'concession',
                'app_id',
                'exploration_name',
                'east_red',
                'north_red'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )    

        class Meta:
            model = WellGeoinfo
            # readonly_fields = ['well_id', ]
            fields = ['well_id','concession',
            'app_id' ,'exploration_name',
            'egpc_name','spud_date','lat_red','long_red','east_red','north_red',
            'elevation','well_type','well_status']
            widgets = {
                'spud_date': forms.DateInput(attrs={'class':'datepicker1','type':'date'}),}





class wellcreate_form(ModelForm):
    # spud_date = forms.DateTimeField(
    #         label='spud_date',
    #     widget=forms.widgets.DateInput(attrs={'type':'date'}),
    #     )
    def __init__(self, *args, **kwargs):
        super(wellcreate_form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # self.fields['well_status'].widget.attrs['readonly'] = True
            self.fields['concession'].required = True
            self.fields['exploration_name'].required = True
            self.fields['well_status'].required = False
            self.fields['well_status'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = WellGeoinfo
        # readonly_fields = ['well_id','well_status',]
        fields = ['well_id','concession',
        'exploration_name',
        'well_type','well_status','deviated',
        'spud_date',
        'well_remarks']

        widgets = {
            'spud_date': forms.DateInput(attrs={'class':'datepicker1','type':'date'}),}
 

class Well_Form2(ModelForm):
    
    
    class Meta:
        model = WellGeoinfo
        readonly_fields = ['well_id', ]
        fields = ['well_id','concession',
        'app_id' ,'exploration_name',
        'egpc_name','east_red','north_red',
        'elevation','well_type','well_status']
    
 
class Well_Form(ModelForm):
    
    
    class Meta:
        model = WellGeoinfo
        readonly_fields = ['well_id', ]
        fields = ['well_id','concession','app_id' ,'exploration_name',
        'egpc_name','east_red','north_red','elevation','well_type','well_status']
       
    # def __init__(self,wellobj,*args,**kwargs):
    def __init__(self,well,*args,**kwargs):
    
        super (Well_Form,self ).__init__(*args,**kwargs) # populates the post
        self.fields['app_id'].queryset = Approved.objects.filter(well_info=well)



class wellDetail_form(ModelForm):

    # date =forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    wellid_calc = forms.IntegerField(
        label='well_id',
        widget=forms.TextInput(attrs={'style': 'width:8ch','placeholder': ''}))

    formatedlat = forms.CharField(
        label='Egy07 Latitude',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    formatedlong = forms.CharField(
        label='Egy07 Longitude',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    lat_EG_dd = forms.CharField(
        label='lat_EG_dd',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    long_EG_dd = forms.CharField(
        label='long_EG_dd',
        widget=forms.TextInput(attrs={'placeholder': ''}))

    formatedlatWGS84 = forms.CharField(
        label='WGS84 Latitude',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    formatedlongWGS84 = forms.CharField(
        label='WGS84 Longitude',
        widget=forms.TextInput(attrs={'placeholder': ''}))
 
    appeast = forms.CharField(
        label='App East',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    appnorth = forms.CharField(
        label='App North',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    finalstake_del_N = forms.CharField(
        label='Staked Final Delta N',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    finalstake_del_E = forms.CharField(
        label='Staked Final Delta E',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    finalstake_del_Elev = forms.CharField(
        label='Staked Final Delta Elev',
        widget=forms.TextInput(attrs={'placeholder': ''}))

    east_shape = forms.CharField(
        label='east shape',
        widget=forms.TextInput(attrs={'placeholder': ''}))

   # def save(self, commit=True):
    #     model_instance = super(wellDetail_form, self).save(commit=False)
    #     result = super(wellDetail_form, self).save(commit=True)
    #     model_instance.formatedlat = self.cleaned_data['formatedlat']
    #     model_instance.save()
    #     return result

    def __init__(self, *args, **kwargs):
        # self.parent = kwargs.pop('parent', None)

        super(wellDetail_form, self).__init__(*args, **kwargs)
        
        

        self.helper = FormHelper()
        self.helper.form_tag = False
        # helper.form_method = 'post'
        # self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Row(
                #'date',
                Column('concession', css_class='form-group col-md-1.5 mb-0'),
                Column('wellid_calc', css_class='form-group col-md-0.5 mb-0'),
                Column('exploration_name', css_class='form-group col-md-1.5 mb-0'),
                Column('egpc_name', css_class='form-group col-md-1.5 mb-0'),
                Column('production_name', css_class='form-group col-md-1.5 mb-0'),
                # Column('', css_class='form-group col-md-2 mb-0'),
                Column('app_id', css_class='form-group col-md-1.5 mb-0'),
                Column('appeast', css_class='form-group col-md-1.5 mb-0'),
                Column('appnorth', css_class='form-group col-md-1.5 mb-0'),

                css_class='form-row'
            ),
            
           
            Row(
                Column('lat_red', css_class='form-group col-md-1.5 mb-0'),
                Column('long_red', css_class='form-group col-md-1.5 mb-0'),
                Column('lat_EG_dd', css_class='form-group col-md-1.5 mb-0'),
                Column('long_EG_dd', css_class='form-group col-md-1.5 mb-0'),
                Column('formatedlat', css_class='form-group col-md-1.5 mb-0'),
                Column('formatedlong', css_class='form-group col-md-1.5 mb-0'),
                Column('formatedlatWGS84', css_class='form-group col-md-1.5 mb-0'),
                Column('formatedlongWGS84', css_class='form-group col-md-1.5 mb-0'),
                css_class='form-row'
            ),

            Row(

                Column('east_red', css_class='form-group col-md-1.5 mb-0'),
                Column('north_red', css_class='form-group col-md-1.5 mb-0'),
                Column('elevation', css_class='form-group col-md-1.5 mb-0'),
                Column('finalstake_del_E', css_class='form-group col-md-1.5 mb-0'),
                Column('finalstake_del_N', css_class='form-group col-md-1.5 mb-0'),
                Column('finalstake_del_Elev', css_class='form-group col-md-1.5 mb-0'),
                Column('east_shape', css_class='form-group col-md-1.5 mb-0'),
                css_class='form-row'
            ),

            Row(
                Column('spud_date', css_class='form-group col-md-1.2 mb-0'),
                Column('rig', css_class='form-group col-md-1 mb-0'),
                Column('well_type', css_class='form-group col-md-1.5 mb-0'),
                Column('deviated', css_class='form-group col-md-1.5 mb-0'),
                Column('well_status', css_class='form-group col-md-1.2 mb-0'),
                Column('issued_date', css_class='form-group col-md-1.2 mb-0'),
                Column('issued_by', css_class='form-group col-md-1.2 mb-0'),
                Column('well_remarks', css_class='form-group col-md-3.1 mb-0'),
                css_class='form-row'
            ),
           
            
            # Submit('submit', 'Sign in'),
        
            # ButtonHolder(
            #     Submit('submit', 'Submit', css_class='button white')),
            # TabHolder(
            #     Tab('t1',
            #         HTML('{% block options %} {% endblock %}'),
            #         # 'meridian_conv',
            #         'spud_date',
            #         ),
            #     Tab('t2',
            #         # 'magnetic_dec',
            #         #    'well_status',
            #         ),
            #     Tab('t3',
            #         # 'heightreference',
            #         # 'rig',
            #         )
            # ),            


            # Fieldset(
            #     'Test Helper Header',
            #     'concession',
            #     'exploration_name',
            #     'east_red',
            #     'north_red'
            # ),
        
            
        )
        # self.template = 'bootstrap/table_inline_formset.html'
        # You can dynamically adjust your layout
        # helper.layout.append(Submit('save', 'save'))
        self.fields['wellid_calc'].widget.attrs['readonly'] = True
        self.fields['wellid_calc'].required = False
        # self.fields['chkid_calc'].widget.attrs['disabled'] = 'disabled'

        instance = getattr(self, 'instance', None)
        
        wellid_2 = getattr(instance, 'well_id')
        self.initial['wellid_calc'] =  wellid_2

        self.fields['concession'].widget.attrs['readonly'] = True
        self.fields['lat_red'].widget.attrs['readonly'] = True
        self.fields['long_red'].widget.attrs['readonly'] = True
        self.fields['lat_EG_dd'].widget.attrs['readonly'] = True
        self.fields['long_EG_dd'].widget.attrs['readonly'] = True
        self.fields['east_red'].widget.attrs['readonly'] = True
        self.fields['north_red'].widget.attrs['readonly'] = True
        # self.fields['elevation'].widget.attrs['readonly'] = True
        self.fields['formatedlat'].widget.attrs['readonly'] = True
        self.fields['formatedlong'].widget.attrs['readonly'] = True
        self.fields['appeast'].widget.attrs['readonly'] = True
        self.fields['appnorth'].widget.attrs['readonly'] = True
        self.fields['finalstake_del_N'].widget.attrs['readonly'] = True
        self.fields['finalstake_del_E'].widget.attrs['readonly'] = True
        self.fields['finalstake_del_Elev'].widget.attrs['readonly'] = True
        
        self.fields['east_shape'].widget.attrs['readonly'] = True

        self.fields['formatedlatWGS84'].widget.attrs['readonly'] = True
        self.fields['formatedlongWGS84'].widget.attrs['readonly'] = True
        
        self.fields['formatedlatWGS84'].widget.attrs['style'] = 'background-color: yellow'
        self.fields['formatedlongWGS84'].widget.attrs['style'] = 'background-color: yellow'
        self.fields['formatedlat'].widget.attrs['style'] = 'background-color: cyan'
        self.fields['formatedlong'].widget.attrs['style'] = 'background-color: cyan'

        self.fields['formatedlat'].required = False
        self.fields['formatedlong'].required = False
        
        self.fields['lat_EG_dd'].required = False
        self.fields['long_EG_dd'].required = False

        self.fields['formatedlatWGS84'].required = False
        self.fields['formatedlongWGS84'].required = False
        self.fields['appeast'].required = False
        self.fields['appnorth'].required = False
        self.fields['finalstake_del_N'].required = False
        self.fields['finalstake_del_E'].required = False
        self.fields['finalstake_del_Elev'].required = False

        self.fields['east_shape'].required = False

        self.fields['issued_date'].required = False
        self.fields['issued_by'].required = False
        self.fields['issued_by'].input_formats=('%d/%m/%Y', )
        self.fields['issued_by'].widget.format='%d/%m/%Y'
        self.fields['heightreference'].required = False
        self.fields['deviated'].required = False
        self.fields['meridian_conv'].required = False
        self.fields['magnetic_dec'].required = False

        
        

        
        self.fields['app_id'].queryset = Approved.objects.filter(well_info=instance.pk)
        self.fields['app_id'].required = False
        self.fields['app_id'].widget.attrs['disabled'] = 'disabled'
        # self.fields['app_id'].widget.attrs['readonly'] = True
        
        remarks = "1-Distance to _______ plant is about ______ Km on tracks.\n"
        remarks = remarks + "2-Track length is about _____ km.\n"
        remarks = remarks + "3-Direct distance to ____ WW is ____ km to ________direction\n"
        field_value = getattr(instance, 'well_remarks')
        if not field_value:
            self.initial['well_remarks']=remarks
        
       
        appidvalue = getattr(instance, 'app_id')
        lat_field_value = getattr(instance, 'lat_red')
        long_field_value = getattr(instance, 'long_red')
        
        if instance and instance.pk and appidvalue and lat_field_value and long_field_value:            
            self.initial['lat_EG_dd'] = bap_lib.ddmmss_to_dd(lat_field_value) # (latstr[:2] + "°" + latstr[2:4] + "'" + latstr[4:] + "\" N")
            self.initial['long_EG_dd'] =bap_lib.ddmmss_to_dd(long_field_value) # (longstr[:2] + "°" + longstr[2:4] + "'" + longstr[4:] + "\" E")
 
            epsg_From = 22992 # RedBelt
            epsg_To = 22992 # RedBelt
            # Edit by Nader check app_id exist or not -------
            xlong_to,ylat_to,zcart_to,long1_to,lat1_to,zcart2_to = bap_lib.coord_conv(epsg_From,epsg_To,instance.east_red,instance.north_red)
            # print("PPPPPPPPPPP ",long1_to,lat1_to)
            if lat1_to and long1_to:
                self.initial['formatedlat'] = lat1_to # (latstr[:2] + "°" + latstr[2:4] + "'" + latstr[4:] + "\" N")
                self.initial['formatedlong'] =long1_to # (longstr[:2] + "°" + longstr[2:4] + "'" + longstr[4:] + "\" E")

            # Edit by Nader check app_id exist or not -------
            if instance.app_id:
                self.initial['appeast'] = bap_lib.decimal_places(instance.app_id.app_east,2) # str(format(instance.app_id.app_east , '.2f')).zfill(6) #.filter(app_type='Final').first().app_east
                self.initial['appnorth'] = bap_lib.decimal_places(instance.app_id.app_north,2) # str(format(instance.app_id.app_north, '.2f')).zfill(6)   #.filter(app_type='Final').first().app_east

                self.initial['east_red'] = bap_lib.decimal_places(instance.east_red,2) #str(format(instance.east_red , '.2f')).zfill(6) #.filter(app_type='Final').first().app_east
                self.initial['north_red'] = bap_lib.decimal_places(instance.north_red,2) #str(format(instance.north_red, '.2f')).zfill(6)   #.filter(app_type='Final').first().app_east


            east_field_value = getattr(instance, 'east_red')
            north_field_value = getattr(instance, 'east_red')
            if east_field_value and north_field_value:                 
               # epsg_from_prov = instance.app_id.projection.epsg
                epsg_From = 22992 # RedBelt
                epsg_To = 4326 # WGS84
                # Edit by Nader check app_id exist or not -------
                xlong_to,ylat_to,zcart_to,long_to,lat_to,zcart2_to = bap_lib.coord_conv(epsg_From,epsg_To,instance.east_red,instance.north_red)

                wgs84Lat = lat_to
                wgs84Long =  long_to
                self.initial['formatedlatWGS84'] =wgs84Lat# (wgs84Lat[:2] + "°" + wgs84Lat[2:4] + "'" + wgs84Lat[4:] + "\" N")
                self.initial['formatedlongWGS84'] = wgs84Long# (wgs84Long[:2] + "°" + wgs84Long[2:4] + "'" + wgs84Long[4:] + "\" E")
 
                if instance.staked_set.filter(st_type='Final').count()>0:
                    if instance.staked_set.filter(st_type='Final').first().st_east:
                        app_st_E= instance.staked_set.filter(st_type='Final').first().st_east - instance.app_id.app_east
                        app_st_N=instance.staked_set.filter(st_type='Final').first().st_north - instance.app_id.app_north
                        app_st_elev=instance.staked_set.filter(st_type='Final').first().st_elev - instance.app_id.app_elev
                        #finalstake_del_Elev
                    # str(format(csec, '.3f')).zfill(6)
                        self.initial['finalstake_del_E'] = str(format(app_st_E, '.4f')).zfill(6) 
                        self.initial['finalstake_del_N'] = str(format(app_st_N, '.4f')).zfill(6) 
                        self.initial['finalstake_del_Elev'] = str(format(app_st_elev, '.4f')).zfill(6) 

                        self.initial['east_shape'] = str(format(app_st_elev, '.4f')).zfill(6)                         

                else:
                    self.initial['finalstake_del_E'] = "N/A"
                    self.initial['finalstake_del_N'] = "N/A"
                    self.initial['finalstake_del_Elev'] = "N/A"

                    self.initial['east_shape'] = "N/A"

    # def clean_app_id(self):
    #     # As shown in the above answer.
    #     instance = getattr(self, 'instance', None)
    #     if instance:
    #         return instance.app_id
    #     else:
    #         return self.cleaned_data.get('app_id', None)
    
    # def clean_app_id(self):
    #     if self.instance:
    #         if self.instance.app_id is not None:
    #             return self.instance.app_id
    #         else:
    #             return None
    #     else:
    #         return self.fields['app_id']

    def clean_app_id(self):
        
        if self.instance:
            if self.instance.app_id is not None:
            # if self.instance.app_id:
                # print ("I'm here")
                return self.instance.app_id
            else:
                # print ("I'm here in else1")
                # raise forms.ValidationError("No data for app_id")
                # return self.fields['app_id']
                return None
            
        else:
            if self.fields['app_id']:
                return self.fields['app_id']
            else:
                # print ("I'm here in else2")
                return None


                
    # def clean_app_id(self):
    #     app_id = self.cleaned_data['app_id']
    #     # if User.objects.filter(app_id=app_id).exists():
    #     #     raise ValidationError("Email already exists")
    #     # return app_id
    #     return app_id
    # def clean_well_remarks(self):
    #     remarks = self.cleaned_data['well_remarks']
    #     if not remarks:# or len(remarks) == 0 :
    #         remarks = "1-Distance to _______ plant is about ______ Km on tracks.\n"
    #         remarks = remarks + "2-Track length is about _____ km.\n"
    #         remarks = remarks + "3-Direct distance to ____ WW is ____ km to ________direction\n"
    
    #         #     raise ValidationError("Email already exists")
    #         # return remarks
    #     return remarks
    class Meta(object):
        model = WellGeoinfo
        readonly_fields = ['well_id', 'concession']
        fields = ['heightreference','issued_date','issued_by','deviated','meridian_conv',
        'magnetic_dec','formatedlat','appeast','formatedlong','well_id','concession',
        'app_id' ,'exploration_name','egpc_name','production_name','rig','spud_date',
        'lat_red','long_red','lat_EG_dd','long_EG_dd','formatedlatWGS84','formatedlongWGS84','east_red','north_red',
        'elevation','well_type','well_status','well_remarks']
        
        widgets = {
            'spud_date': forms.DateInput(attrs={'class':'datepicker1','type':'date'}),
            # 'issued_date': forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'datepicker1','type':'date'}),
            'issued_date': forms.DateInput(attrs={'class':'datepicker1','type':'date'}),
            'well_remarks': forms.Textarea(attrs={'placeholder': 'well_remarks', "rows":5, "cols":100}),
            # 'Formatedlat': forms.TextInput(),
            # 'app_id': forms.HiddenInput (),
            }


class ApprovedForm(ModelForm):
    appid_calc = forms.IntegerField(
        label='app_id',
        widget=forms.TextInput(attrs={'style': 'width:8ch','placeholder': ''}))

    def __init__(self, *args, **kwargs):
    
        super(ApprovedForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('prov_name', css_class='form-group col-md-2 mb-0'),
                Column('app_name', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ))
        
        self.fields['app_inline'].widget.attrs['readonly'] = True
        self.fields['app_xline'].widget.attrs['readonly'] = True
        self.fields['appid_calc'].widget.attrs['readonly'] = True
        self.fields['appid_calc'].required = False
        self.fields['app_remarks'].required = False
        self.fields['prov_date'].required = False


        # self.fields['prov_date'].input_formats=('%d/%m/%Y',)
        # self.fields['prov_date'].widget.format='%d/%m/%Y'

        self.fields['appid_calc'].widget.attrs['disabled'] = 'disabled'
        self.fields['app_type'].widget.attrs['readonly'] = True
    
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            
            appid_2 = getattr(instance, 'app_id')
            self.initial['appid_calc'] =  appid_2
       
    def clean_app_id(self):
        app_id = self.cleaned_data['app_id']
        # if User.objects.filter(app_id=app_id).exists():
        #     raise ValidationError("Email already exists")
        # return app_id
        return app_id

    class Meta:
        model = Approved
        # readonly_fields = ['app_id','prov_id','app_date', ]
        fields = ['appid_calc','app_id','prov_name','app_name','prov_from',
         'projection','prov_date',
         'prov_seismic_survey',
         'app_inline','app_xline','app_lat','app_long',
         'app_east','app_north','app_elev',
         'app_type','app_remarks'
         ]
        
        widgets = {
            # 'app_date': forms.DateInput(format=('%d-%b-%Y'),attrs={'class':'datepicker','type':'text'}),
            # 'app_date': forms.DateInput(attrs={'class':'datepicker','type':'date'}),
            'prov_date': forms.DateInput(attrs={'class':'datepicker1','style': 'width:20ch','type':'date'}),
            # 'prov_date': forms.DateInput(format=('%d-%b-%Y'),attrs={'class':'datepicker1','style': 'width:20ch','type':'text'}),
            # 'prov_date': forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'datepicker1','style': 'width:20ch','type':'text'}),
            # ,input_formats=('%d-%b-%Y', )
            # 'projection': forms.TextInput (attrs={'type':'date'),
            'app_type': forms.HiddenInput(),
            'app_east': forms.TextInput (),
            'app_north': forms.TextInput (),
            'app_lat': forms.TextInput (),
            'app_long': forms.TextInput (),
            'app_elev': forms.TextInput (attrs={'style': 'width:10ch'}),
            'prov_name': forms.TextInput (attrs={'style': 'width:15ch','placeholder': ''}),
            'app_name': forms.TextInput (attrs={'style': 'width:15ch','placeholder': ''}),
            'app_remarks': forms.Textarea(attrs={'placeholder': 'app_remarks', "rows":1, "cols":20}),       

            }



ApprovedFormSet = inlineformset_factory(WellGeoinfo, Approved,
                                            form=ApprovedForm, extra=1,can_delete = True)


class StakeoutForm(ModelForm):
    stid_calc = forms.IntegerField(
        label='st_id',
        widget=forms.TextInput(attrs={'style': 'width:8ch','placeholder': ''}))
    expname_calc = forms.CharField(
        label='ExpName',
        widget=forms.TextInput(attrs={'style': 'width:8ch','placeholder': ''}))

    def __init__(self, *args, **kwargs):
            # self._wellvar = kwargs.pop('wellvar', None)

            super(StakeoutForm, self).__init__(*args, **kwargs)
            
            self.fields['stid_calc'].widget.attrs['readonly'] = True
            self.fields['stid_calc'].required = False
            self.fields['stid_calc'].widget.attrs['disabled'] = 'disabled'
            
            self.fields['expname_calc'].widget.attrs['readonly'] = True
            self.fields['expname_calc'].required = False
            self.fields['expname_calc'].widget.attrs['disabled'] = 'disabled'
            # self.fields['expname_calc'].required = False
            # self.fields['app'].required = False


            instance = getattr(self, 'instance', None)
            if instance:
                # self.fields['app'].queryset = Approved.objects.filter(well_info=instance.well_info)
                # print ("I'm in Instance KKKKKKKKKKKKKKKKKK")
                # print (instance.well_info)
                pass

            if instance and instance.pk:
                
                
                stid_2 = getattr(instance, 'st_id')
                # expname=getattr(instance, 'exploration_name')
                self.initial['stid_calc'] =  stid_2
                
                expname= instance.well_info.exploration_name
                self.initial['expname_calc'] =  expname
            # else:
            #     pass
                # self.fields['app'].queryset = Approved.objects.filter(well_info=0)
                
                # self.fields['st_type'].widget.attrs['readonly'] = True
    
    # def clean_app(self):
        
    #     app= self.cleaned_data['app']
    #     return app

    # def clean_app(self):
    #     if self.instance:
    #         if self.instance.app:
    #             # return Approved.objects.filter(pk=self.instance.app).first()
    #             return self.instance.app
    #         else:
    #             return None
    #     else:
    #         # return self.fields['app']
    #         if self.fields['app']:
    #             return self.fields['app']
    #         else:
    #             print ("I'm here in else2")
    #             return None


    # def clean_app(self):
    #     if self.instance:
    #         if self.instance.app is not None:
    #         # if self.instance.app_id:
    #             print ("I'm here")
    #             return self.instance.app
    #         else:
    #             print ("I'm here in else111")
    #             # raise forms.ValidationError("No data for app_id")
    #             # return self.fields['app_id']
    #             return  None
            
    #     else:
    #         if self.fields['app']:
    #             return self.fields['app']
    #         else:
    #             print ("I'm here in else2")
    #             return None


    class Meta:
        model = Staked
        # readonly_fields = ['app_id','prov_id','app_date', ]
        fields = ['stid_calc','expname_calc','st_id','st_east','st_north','st_elev','st_date',
        'st_by','st_sv','st_type','app','st_remarks'
         ]
        
        widgets = {
            'st_date': forms.DateInput(attrs={'class':'datepicker1','style': 'width:20ch','type':'date'}),
            'st_east': forms.TextInput (),
            'st_north': forms.TextInput (),
            'st_elev': forms.TextInput (attrs={'style': 'width:10ch'}),
            # 'st_by': forms.CheckboxSelectMultiple(),
            'st_remarks': forms.Textarea(attrs={'placeholder': 'st_remarks', "rows":1, "cols":20}),
            }



StakeoutFormSet = inlineformset_factory(WellGeoinfo, Staked,
                                            form=StakeoutForm, extra=1)



class CheckForm(ModelForm):
    chkid_calc = forms.IntegerField(
        label='ch_id',
        widget=forms.TextInput(attrs={'style': 'width:8ch','placeholder': ''}))

    def __init__(self, *args, **kwargs):

    
        super(CheckForm, self).__init__(*args, **kwargs)
        
        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
            # self.fields['st_type'].widget.attrs['readonly'] = True
        self.fields['chkid_calc'].widget.attrs['readonly'] = True
        self.fields['chkid_calc'].required = False
        self.fields['chkid_calc'].widget.attrs['disabled'] = 'disabled'

        # self.fields['st'].required = False
        
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # self.fields['st'].queryset = Staked.objects.filter(well_info=instance.well_info)

            chid_2 = getattr(instance, 'chk_id')
            self.initial['chkid_calc'] =  chid_2
        else:
            pass
            # self.fields['st'].queryset = Staked.objects.filter(well_info=0)

    def clean_st(self):
        st_id = self.cleaned_data['st']
        # if User.objects.filter(app_id=app_id).exists():
        #     raise ValidationError("Email already exists")
        # return app_id
        return st_id

    # def clean_st(self):
    #     st = self.cleaned_data['st']
    #     # if User.objects.filter(app_id=app_id).exists():
    #     #     raise ValidationError("Email already exists")
    #     # return app_id
    #     return st

    # def clean_st(self):
    #     if self.instance:
    #         if self.instance.st is not None:
    #         # if self.instance.app_id:
    #             print ("I'm here")
    #             return self.instance.st
    #         else:
    #             print ("I'm here in else1")
    #             # raise forms.ValidationError("No data for app_id")
    #             # return self.fields['app_id']
    #             return None
            
    #     else:
    #         if self.fields['st']:
    #             return self.fields['st']
    #         else:
    #             print ("I'm here in else2")
    #             return None


    class Meta:
        model = Checked
        # readonly_fields = ['app_id','prov_id','app_date', ]
        fields = ['chkid_calc','chk_id','chk_east','chk_north','chk_elev','chk_cellar_pno',
        'chk_date','chk_by','chk_sv','st','chk_remarks'
         ]
        
        widgets = {
            'chk_date': forms.DateInput(attrs={'class':'datepicker1','style': 'width:20ch','type':'date'}),
            'chk_east': forms.TextInput (),
            'chk_north': forms.TextInput (),
            'chk_elev': forms.TextInput (attrs={'style': 'width:10ch'}),
            'chk_remarks': forms.Textarea(attrs={'placeholder': 'chk_remarks', "rows":1, "cols":20}),
            
            }



CheckFormSet = inlineformset_factory(WellGeoinfo, Checked,
                                            form=CheckForm, extra=1)                                            



class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = 'datetimepicker_{name}'.format(name=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context


class coord_conv_form(forms.Form):

    inputX_Long = forms.FloatField(
        label='Input Easting(X) or Longitude (ddmmss.sss)',
        # widget=forms.TextInput(attrs={'style': 'width:20ch','placeholder': 'X or Longitude(ddmmss.ss)'}))
        widget=forms.TextInput(attrs={'placeholder': 'X or Longitude(example:300120.012)'}))
    inputY_Lat = forms.FloatField(
        label='Input Northing(Y) or Latitude (ddmmss.sss)',
        widget=forms.TextInput(attrs={'placeholder': 'Y or Latitude(example:300120.012)'}))
    outputX = forms.CharField(
        label='Output Easting(X)',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    outputY = forms.CharField(
        label='Output Northing(Y)',
        widget=forms.TextInput(attrs={'placeholder': ''}))
 
    outputLong = forms.CharField(
        label='Output Longitude(X)',
        widget=forms.TextInput(attrs={'placeholder': ''}))
    outputLat = forms.CharField(
        label='Output Latitude(Y)',
        widget=forms.TextInput(attrs={'placeholder': ''}))

    psd1 = forms.ModelChoiceField(
        queryset=Psd.objects.all(),
        # to_field_name="epsg"
    )
    psd2 = forms.ModelChoiceField(
        queryset=Psd.objects.all(), 
        # to_field_name="epsg"
    )

    radio_buttons_Input = forms.ChoiceField(
        label = "Input Format",
        choices = (
            (1, "Geographic"), 
            (2, "Grid")
        ),
        widget = forms.RadioSelect,
        initial = 2,
    )


    def __init__(self, *args, **kwargs):
        # self.parent = kwargs.pop('parent', None)
        super(coord_conv_form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        print(instance)
        if instance:
            print("Instance AAAAAAAAAAAA")
        # print('formClass')
        # self.fields['outputX_long'].initial = '8888'
        # self.fields['outputX_long'].initial =  'override'

 


        self.helper = FormHelper()
        self.helper.form_tag = False
        # helper.form_method = 'post'
        # self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Row(
                    #'date',
                    Column('radio_buttons_Input', css_class='form-group col-md-3 mb-0 ml-2'),
                    # Column('radio_buttons_Output', css_class='form-group col-md-3 mb-0'),
                    css_class='form-row'
                ),
  
                Row(
                    #'date',
                    Column('inputX_Long', css_class='form-group col-md-3 mb-0 ml-2'),
                    Column('inputY_Lat', css_class='form-group col-md-3 mb-0 ml-2'),
                    css_class='form-row'
                ),
              
                Div(
                    Column('psd1', css_class='form-group col-md-4 mb-0 ml-2'),
                    Column('psd2', css_class='form-group col-md-4 mb-0 ml-2'),
                    css_class='card'
                    # css_id = 'special-fields'
                ),    
               
                # <button class="btn btn-danger pull-right" style="width: 20%; height: 50px" type="submit" >Calculate</button> <br/> <br/> 
                ButtonHolder(
                    Submit('submit', 'Calculate', css_class='button white')
                ),
                #  Row(
                #     #'date',
                #     Column('outputX', css_class='form-group col-md-3 mb-0'),
                #     Column('outputY', css_class='form-group col-md-3 mb-0'),
                #     css_class='form-row'
                # ),
                # Row(
                #     #'date',
                #     Column('outputLat', css_class='form-group col-md-3 mb-0'),
                #     Column('outputLong', css_class='form-group col-md-3 mb-0'),
                #     css_class='form-row'
                # ),
          
            )
        self.fields['outputY'].required = False
        # self.fields['outputY'].widget.attrs['disabled'] = True
        # self.fields['outputY'].widget.attrs['readonly'] = True
        self.fields['outputX'].required = False
        # self.fields['outputX'].widget.attrs['disabled'] = True
        # self.fields['outputX'].widget.attrs['readonly'] = True
        self.fields['outputLat'].required = False
        self.fields['outputLong'].required = False    
   
            
    # def clean_outputLong(self):
    #     outputLong = self.cleaned_data['outputLong']
    #     return outputLong
    
    # def clean_outputLat(self):
    #     outputLat = self.cleaned_data['outputLat']
    #     return outputLat

    # def clean_outputX(self):
    #     outputX = self.cleaned_data['outputX']
    #     return outputX
    
    # def clean_outputY(self):
    #     outputY = self.cleaned_data['outputY']
    #     return outputY


    def save(self, commit=True):
        # instance = super(coord_conv_form, self).save(commit=False)
        # instance.flag1 = 'flag1' in self.cleaned_data['multi_choice'] # etc
        # if commit:
            # instance.save()
        # return instance
        pass


    def is_valid(self):
        # run the parent validation first
        valid = super(coord_conv_form, self).is_valid()
        # self.outputX = "self.cleaned_data['outputX']"
        # we're done now if not valid
        return True

    def clean(self):
        # cleaned_data = suer().clean()#self.clean()
        # super().clean()
        super(coord_conv_form, self).clean() 
        x1 = self.cleaned_data.get("inputX_Long")
        y1 = self.cleaned_data.get("inputY_Lat")

        if  x1 and  y1 :
            Input_eastX= x1
            Input_northY= y1

            psd_From =  self.cleaned_data.get("psd1")
            psd_To =  self.cleaned_data.get("psd2")
            
            inputFormat =  self.cleaned_data.get("radio_buttons_Input")#form.cleaned_data['radio_buttons_Input']
            # Edit by Nader check app_id exist or not -------
            xlong_to,ylat_to,zcart_to,long_to,lat_to,zcart2_to = bap_lib.coord_conv(psd_From.epsg,psd_To.epsg,Input_eastX,Input_northY)
            
            self.cleaned_data['outputX'] =   str(xlong_to)
            self.cleaned_data['outputY'] =   str(ylat_to)
            self.cleaned_data['outputLat'] =   str(lat_to)
            self.cleaned_data['outputLong'] =   str(long_to)
      
        return self.cleaned_data 

    class Meta:
            
            # readonly_fields = ['well_id', ]
            fields = ['inputX_Long','inputY_Lat','psd1','psd2','outputX','outputY','outputLat','outputLong']
            # widgets = {
            #     # 'spud_date': forms.DateInput(attrs={'class':'datepicker1','type':'date'}),
            #     'outputX_long': forms.TextInput(attrs={'disabled':'true'}) ,
                
                
            #     }
            
     