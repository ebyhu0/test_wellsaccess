
from django.contrib import admin
from django.urls import path
from . import views as well_views
from . import bap_lib
from rest_framework import routers
from .api import PSDViewSet

# from views import AddWellView, index, about, home

# app_name = 'wells'


router = routers.DefaultRouter()
router.register('api/psd', PSDViewSet, 'psd')

urlpatterns = [


    path('concstable/', well_views.ConcstableView.as_view(), name='table-concs'),
    path('concstablelist/', well_views.ConcstableListView.as_view(),
         name='tablelist-concs'),

    path('delete_item/<pk>', well_views.delete_item, name='delete_item'),
    path('add_to_cart/<pk>', well_views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<pk>', well_views.delete_from_cart,
         name='delete_from_cart'),



    path('wellstable/<conc_id>',
         well_views.WellstableView.as_view(), name='table-wells'),
    path('wellstablelist/<conc_id>',
         well_views.WellstableListView.as_view(), name='tablelist-wells'),
    path('Welllist_filter/<conc_id>',
         well_views.Welllist_filter.as_view(), name='Welllist_filter'),
    path('Wellstable_filter/', well_views.Wellstable_filter.as_view(),
         name='Wellstable_filter'),
    path('WellsInConc_table_filter/<conc_id>',
         well_views.WellsInConc_table_filter, name='WellsInConc_table_filter'),

    path('addMultiple_ToCart/', well_views.addMultiple_ToCart,
         name='addMultiple_ToCart'),
    path('selectedWellscart/', well_views.selectedWellsCart,
         name='selectedWellscart'),
    path('crispywell/<pk>', well_views.crispformdef, name='crispywell'),
    path('wellupdate/<pk>', well_views.WellUpdateView.as_view(),
         name='update-well-view'),
    path('setfinal/<app_id>', bap_lib.SetFinal, name='set_final'),
    # path('setfinal_stake/<st_id>', bap_lib.Set_final_stake, name='set_final_stake'),
    # path('setfinal_check/<chk_id>', bap_lib.Set_final_check, name='set_final_check'),


    path('well/new/', well_views.AddWellView.as_view(), name='add-well'),

    path('well/newinconc/<conc_id>',
         well_views.CreateWell_inConc.as_view(), name='add-well-conc'),
    path('well/addnew/', well_views.CreateWell.as_view(), name='well-addnew2'),

    path('', well_views.home, name='bx-home'),
    path('about/', well_views.about, name='bx-about'),


    path('crispformdef/<pk>', well_views.crispformdef, name='crispformdef'),
    # path('crispformcls/<pk>', well_views.crispformcls_view.as_view(), name='crispform_view2'),


    # path('wells/', well_views.WellListView.as_view(), name='list-well'),
    # path('concs/', well_views.ConcListView.as_view(), name='list-concs'),
    # path('conc/<int:pk>', well_views.ConcWells_pp, name='list-concwells'),
    path('coordconv/', well_views.coordconv, name='coordconv'),
]

urlpatterns += router.urls
