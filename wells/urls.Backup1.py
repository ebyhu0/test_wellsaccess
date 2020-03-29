
from django.contrib import admin
from django.urls import path
from . import views as well_views
# from views import AddWellView, index, about, home


urlpatterns = [
    path('', well_views.home, name='bx-home'),
    # path('conc/<int:conc_id>', well_views.ConcessionWellsList.as_view(), name='list-concwells'),
    path('conc/<int:pk>', well_views.ConcWells_pp, name='list-concwells'),

    # path('', WellsListView.as_view(), name='bx-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('well/new/', well_views.AddWellView.as_view(), name='add-well'),
    path('wells/', well_views.WellListView.as_view(), name='list-well'),

    path('concs/', well_views.ConcListView.as_view(), name='list-conc'),
    path('concstable/', well_views.ConctableView.as_view(), name='table-conc'),
    path('wellstable/<conc_id>', well_views.WellstableView.as_view(), name='table-wells'),
    # path('welldetail/<pk>', well_views.WellDetailView.as_view(), name='edit-well'),
    path('welldetail_pp/<pk>', well_views.WellDetail_pp, name='edit-well_pp'),



    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', well_views.about, name='bx-about'),
]
