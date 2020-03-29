from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<well_id>', views.cart_add, name='cart_add'),
    path('remove/<well_id>', views.cart_remove, name='cart_remove'),
    path('removeAll/', views.cart_removeAll, name='removeAll'),
    

]