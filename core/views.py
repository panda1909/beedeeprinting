from django.shortcuts import render
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products

from django.http import HttpResponse
from django.template import loader




# Create your views here.

def business_card(request):
    business_card = bc_products.objects.get(id=1)
    
    context = {
        "business_card": business_card,
    }
    return render(request, "core/detail.html", context)

def Home(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
    }
    return render(request, "core/all_products.html", context)

class Aboutus(TemplateView):
    def get(self, request):
        return render(request, 'core/aboutus.html')


class Cart(TemplateView):
    def get(self, request):
        return render(request, 'core/cart.html')
