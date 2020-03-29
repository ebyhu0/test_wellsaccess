from decimal import Decimal
from django.conf import settings
from wells.models import WellGeoinfo


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # print ("PPPPPPPPPPP Checking Cart exist",cart)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.session.modified = True
            # print ("KKKKKKKKKKKKK Creating New Cart",cart)
        self.cart = cart
        
        
    # def add(self, WellGeoinfo, quantity=1, update_quantity=False):
    def add(self, well_id):    
        WellGeoinfo_id = well_id # str(well_id)
        if WellGeoinfo_id not in self.cart:
            self.cart[WellGeoinfo_id] = {'quantity': 0,}#, 'price': str(WellGeoinfo.price)}
        
        # if update_quantity:
        #     self.cart[WellGeoinfo_id]['quantity'] = quantity
        # else:
        #     self.cart[WellGeoinfo_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, well_id):
        WellGeoinfo_id = well_id
        
        if WellGeoinfo_id in self.cart:
            del self.cart[WellGeoinfo_id]
            self.save()

    def removeAll(self):
        # print("FFFFFFFFs",self.cart.keys())
        # Yasser & Nader Comment ----
        # During the Delation process needs to avoid size change we should 
        # copy the dictionary into List to let the iteration works
        for item in list(self.cart):
            del self.cart[item]
 
        self.save()

    def __iter__(self):
        WellGeoinfo_ids = self.cart.keys()
        WellGeoinfos = WellGeoinfo.objects.filter(pk__in=WellGeoinfo_ids)
        for WellGeoinfo in WellGeoinfos:
            self.cart[str(WellGeoinfo.pk)]['WellGeoinfo'] = WellGeoinfo

        # for item in self.cart.values():
            # item['price'] = Decimal(item['price'])
            # item['total_price'] = item['price'] * item['quantity']
            # yield item
            # pass 

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        # return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        pass

    # def clear(self):
    #     del self.session[settings.CART_SESSION_ID]
    #     self.session.modified = True
    