from django.shortcuts import render
from .models import FoamcorePosters, QuotationFoamcorePosters, Products as lf_products

from Business_Cards.models import Products as bc_products
from Business_Stationary.models import Products as bs_products
from Marketing_Products.models import Products as mp_products


# Create your views here.

def FoamCorePostersDetail(request):
    product = lf_products.objects.get(id=4)
    Price_table = QuotationFoamcorePosters.objects.all().distinct()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    menu = QuotationFoamcorePosters.objects.all()
    #menu1 = Extra_features.objects.all()
   
    context = {
    #   Form 
        "menu": menu,
    #   "menu1": menu1,
    #   Price Table    #
        "table" : Price_table,        
    #   side bar content    #
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
    #    Product info   #
        "label" : product.Label,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
    }
    return render(request, "Large_Format_Printing/foamcore_posters.html", context)
