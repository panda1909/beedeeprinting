from django.shortcuts import render
from .models import FoamcorePosters, Products as lf_products

from Business_Cards.models import Products as bc_products
from Business_Stationary.models import Products as bs_products
from Marketing_Products.models import Products as mp_products


# Create your views here.

def FoamCorePostersDetail(request):
    product = lf_products.objects.get(id=4)
<<<<<<< HEAD
    Price_table = QuotationFoamcorePosters.objects.all().distinct()
=======
    Price_table = QuotationFoamcorePosters.objects.all().distinct() 
>>>>>>> eaabd61fb63258282ffe875eff60a7b41f46a9ef
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    menu = QuotationFoamcorePosters.objects.all()
    #menu1 = Extra_features.objects.all()

    size = [1, 2, 4, 5, 6, 7, 8, 9, 10]
    quantity = [100, 200, 400, 500, 600, 700, 800, 900, 1000]
    
    
    dataset = [
        {
            "quantity":100,
            "size":1,
            "price":101,
        },
        {
            "quantity":1000,
            "size":1,
            "price":1001,
        },
        {
            "quantity":500,
            "size":5,
            "price":505,
        },
        {
            "quantity":100,
            "size":10,
            "price":1010,
        },
        {
            "quantity":1000,
            "size":10,
            "price":10100,
        }
    ]
    
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
        "size":size,
        "quantity":quantity,
        "dataset":dataset,
    }
    return render(request, "Large_Format_Printing/foamcore_posters.html", context)
