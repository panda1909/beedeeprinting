from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products 
from Business_Cards.models import business_cards_price, Extra_features
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products

from django.http import HttpResponse
from django.template import loader
from .form import ImageFileUploadForm, BusinessCard



# Create your views here.

def Home(request):
    return render(request, "core/index.html")


def BC_Detail(request):
    
    product = bc_products.objects.get(id=1)
    table = business_cards_price.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    menu = business_cards_price.objects.all()
    menu1 = Extra_features.objects.all()
    
    # if stament for getting info from template

    if request.POST:
        var = request.POST
        #print(var)
        #print('---------')
        printing_type = var['printing_type']
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
        type_quantity_query = business_cards_price.objects.raw('SELECT * FROM Business_Cards_business_cards_price WHERE quantity = %s', [quantity])
        size_query = Extra_features.objects.raw('SELECT id, size_price FROM Business_Cards_Extra_features WHERE size = %s', [size])
        paper_price_query = Extra_features.objects.raw('SELECT id, paper_type_price FROM Business_Cards_Extra_features WHERE paper_type = %s', [paper_type])
        if sides == 'two_sided':
            sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            for u in sides_query:
                print('------Second Side Price--------')
                print(u.second_side_price)
                price_side = u.second_side_price
                break
        else:
            price_side = 0
        for i in paper_price_query:
            print('------Paper Type Price--------')
            print(i.paper_type_price)
            price_paper = i.paper_type_price

        for o in size_query:
            print('------Size Price--------')
            print(o.size_price)
            price_size = o.size_price
        for p in type_quantity_query:
            if printing_type == 'digital_Fast_Discounted':
                print('------Digital Fast Price--------')
                print(p.digital_Fast_Discounted)
                price_type = p.digital_Fast_Discounted
            elif printing_type == 'offset_HQ_Discounted':
                print('------OFFset HQ Price--------')
                print(p.offset_HQ_Discounted)
                price_type = p.offset_HQ_Discounted
                
                
        total_price = (float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_size) * float(quantity)) + price_type
    else:
        total_price = 0
    

    context = {
    #   Total Price and form 
        'total_price' : total_price,
        "menu": menu,
        "menu1": menu1,
    #   Price Table    #
        "table" : table,        
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
    return render(request, "core/detail.html", context)

class Aboutus(TemplateView):
    def get(self, request):
        return render(request, 'core/aboutus.html')

def Checkout(request):
    return render(request, 'core/checkout.html')


def Cart(request):
    return render(request, 'core/cart.html')

# ------  All Products page/funct  ------ # 

def All_products(request):
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

# ------  Catogirze Pages in frontend  ------ # 
# ------  All pages are dynamic using if else and db ------ #

def Business_card(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    bc_card = 1
    bs_card = 0
    lf_card = 0
    mp_card = 0

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card
    }
    return render(request, "core/catogery.html", context)

def Business_stationary(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    bc_card = 0
    bs_card = 1
    lf_card = 0
    mp_card = 0

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card
    }
    return render(request, "core/catogery.html", context)

def Large_format(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    bc_card = 0
    bs_card = 0
    lf_card = 1
    mp_card = 0

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
    }
    return render(request, "core/catogery.html", context)

def Marketing_products(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    bc_card = 0
    bs_card = 0
    lf_card = 0
    mp_card = 1

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card
    }
    return render(request, "core/catogery.html", context)

# ------  Catogirze Pages in frontend  ------ # 
# ------  All pages are dynamic using if else and db ------ #