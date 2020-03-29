from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from .models import Persons,Staked,Seismictype,Operator,HcContent,Companies,Checked,Approved,WellGeoinfo,Concession,Psd,Rig,Seismicvintage,WellType,WellStatus,Bindata

# admin.site.register(Concession)
admin.site.register(Psd)
admin.site.register(Rig)
admin.site.register(Seismicvintage)
admin.site.register(Bindata)
admin.site.register(WellType)
admin.site.register(WellStatus)


# admin.site.register(Approved)
# admin.site.register(Provisional)
admin.site.register(Checked)
admin.site.register(Companies)
admin.site.register(Staked)
admin.site.register(HcContent)
# admin.site.register(Heightreference)
# admin.site.register(MapPsdDescription)
admin.site.register(Operator)
admin.site.register(Seismictype)
admin.site.register(Persons)



@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('content_type')

class ApprovedInline(admin.TabularInline):
    model = Approved
    extra = 0
    # fields=['app_name','app_inline','app_xline','app_east','app_north','app_date','app_type','app_remarks','prov_name','prov_from','prov_interpreter_name','prov_interpreter_dept','prov_seismic_vintage','prov_inline','prov_xline','prov_east','prov_north','projection','prov_date','prov_well_type','prov_type','prov_remarks','prov_spuddate',]
    fields=['prov_interpreter_name','prov_name','app_name','app_inline','app_xline','app_east','app_north','app_date','app_type','app_remarks',]
    ordering = ('app_name',)

# class ProvisionalInline(admin.TabularInline):
#     model = Provisional
#     extra = 0
#     fields=['prov_name','prov_from','prov_interpreter_name','prov_interpreter_dept','prov_seismic_vintage','prov_inline','prov_xline','prov_east','prov_north','projection','prov_date','prov_well_type','prov_type','prov_remarks','prov_spuddate',]
#     ordering = ('prov_name',)
#     # inlines = [ApprovedInline]


class WellGeoinfoInline(admin.TabularInline):
    model = WellGeoinfo
    extra = 0
    fields=['exploration_name','lat_red','long_red','east_red','north_red','elevation','well_type','well_status','rig',]
    ordering = ('exploration_name',)


@admin.register(Concession)
class ConcessionAdmin(admin.ModelAdmin):
    list_display = ('concession', 'operator', 'isactive','concessiontype')
    ordering = ('concession',)
    inlines = [WellGeoinfoInline]

@admin.register(Approved)
class ApprovedAdmin(admin.ModelAdmin):
    readonly_fields = ('app_id',)
    list_display = ('app_name','app_remarks',)
    # fields=['app_name','app_inline','app_xline','app_east','app_north','app_date','app_type','app_remarks','prov_name','prov_from','prov_interpreter_name','prov_interpreter_dept','prov_seismic_vintage','prov_inline','prov_xline','prov_east','prov_north','projection','prov_date','prov_well_type','prov_type','prov_remarks','prov_spuddate',]
    fields=['prov_interpreter_name','prov_name','app_name','app_inline','app_xline','app_east','app_north','app_date','app_type','app_remarks',]
    ordering = ('app_name',)
    # inlines = [ProvisionalInline]

# @admin.register(Provisional)
# class ProvisionalAdmin(admin.ModelAdmin):
#     readonly_fields = ('prov_id',)
#     list_display = ('prov_name',)
#     fields=['prov_name','prov_from','prov_interpreter_name','prov_interpreter_dept','prov_seismic_vintage','prov_inline','prov_xline','prov_east','prov_north','projection','prov_date','prov_well_type','prov_type','prov_remarks','prov_spuddate',]
#     ordering = ('prov_name',)
#     inlines = [ApprovedInline]

@admin.register(WellGeoinfo)
class WellGeoinfoAdmin(admin.ModelAdmin):
    readonly_fields = ('well_id',)
    list_display = ('concession','exploration_name','well_type','well_status',)
    fields = ['exploration_name','lat_red','long_red','east_red','north_red','elevation','well_type','well_status','rig',]
    ordering = ('exploration_name',)
    inlines = [ApprovedInline]
 
    
    # exclude =()


