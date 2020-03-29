from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from wells.models import WellGeoinfo
from .cart import Cart
from .forms import CartAddItemForm
from django.http import HttpResponse

# @require_POST
def cart_add(request,well_id):
    cart = Cart(request)
    # cart = Cart()
    modelItem = get_object_or_404(WellGeoinfo, pk=well_id)
    # form = CartAddItemForm(request.POST)
    # if form.is_valid():
        # cd = form.cleaned_data
        # cart.add (well_id) #(WellGeoinfo=modelItem)#, quantity=cd['quantity'], update_quantity=cd['update'])
    cart.add (well_id)
    # return redirect('cart:cart_detail')
    CurrentPathBeforeLeave = request.META.get('HTTP_REFERER', None) or '/'
    print ("CurrentPathBeforeLeave -------------- ",CurrentPathBeforeLeave)

    return redirect (CurrentPathBeforeLeave)
#     return redirect('selectedWellscart')
    

def items_list(request):
    for item in cart:
        item['update_quantity_form'] = CartAddItemForm() #(initial={'quantity': item['quantity'], 'update': True})


def cart_remove(request, well_id):
    cart = Cart(request)
    # modelItem = get_object_or_404(WellGeoinfo, pk=well_id)
    cart.remove(well_id)
    # return redirect('cart:cart_detail')
    CurrentPathBeforeLeave = request.META.get('HTTP_REFERER', None) or '/'
#     print ("CurrentPathBeforeLeave -------------- ",CurrentPathBeforeLeave)
    return redirect(CurrentPathBeforeLeave)
#      return redirect('selectedWellscart')


def cart_removeAll(request):
    cart = Cart(request)
    # modelItem = get_object_or_404(WellGeoinfo, pk=well_id)
    cart.removeAll()
#     cart.clear()
    # return redirect('cart:cart_detail')
    return redirect('selectedWellscart')


def cart_detail(request):
    cart = Cart(request)
    
    # for item in cart:
    #     item['update_quantity_form'] = CartAddItemForm() #(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
    # return  HttpResponse("I'm in Detail") 