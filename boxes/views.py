from django.shortcuts import redirect, render

from Business_Cards.models import Products as bc_products 
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products
from .models import Products as b_products


# Create your views here.

def Pillow_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    bc_urls = ["business-card-detail" , "edge-painted-detail"]
    bs_urls = [""]
    lf_urls = [""]
    mp_urls = [""]
    b_urls = ["pillow-boxes-detail"]

    bc_aside = zip(bc_urls,bc_object)
    bs_aside = zip(bs_urls,bs_object)
    lf_aside = zip(lf_urls,lf_object)
    mp_aside = zip(mp_urls,mp_object)
    b_aside = zip(b_urls,b_object)


    context ={
        #   side bar content    #
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "b_object"   : b_object,
        #    Product info   #
        "label" : product.Label,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
        #    navbar info   #
        "bc_aside" : bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside" : lf_aside,
        "mp_aside" : mp_aside,
        "b_aside" : b_aside,
    }

    if request.POST:
        request.session['id'] = '1'
        return redirect('b-checkout')


    return render(request, 'boxes/pillow-boxes.html', context)
