from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products 
from Business_Cards.models import edge_painted_business_cards_price, Extra_features
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products

from django.http import HttpResponse
from django.template import loader
#from .form import ImageFileUploadForm, BusinessCard

# Create your views here.

def Edge_painted_Detail(request):
    
    product = bc_products.objects.get(id=2)
    table = edge_painted_business_cards_price.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    menu = edge_painted_business_cards_price.objects.all()
    menu1 = Extra_features.objects.all()
    
    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
        color = var['color']
        
        # queries against relevant options
        # size and quantity price query
        if size == 'US_Standard_Size':
            type_quantity_query = edge_painted_business_cards_price.objects.raw('SELECT id, US_Standard_Size FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        elif size == 'European_Size':
            type_quantity_query = edge_painted_business_cards_price.objects.raw('SELECT id, European_Size FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        elif size == 'Square':
            type_quantity_query = edge_painted_business_cards_price.objects.raw('SELECT id, Square FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])

        # paper type price query
        paper_price_query = Extra_features.objects.raw('SELECT id, paper_type_price FROM Business_Cards_Extra_features WHERE paper_type = %s', [paper_type])

        # Discount query
        discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])

        # sides price query
        if sides == 'two_sided':
            sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            for u in sides_query:
                price_side = u.second_side_price
                break
        else:
            price_side = 0

        
        for i in paper_price_query:
            price_paper = i.paper_type_price

        for o in type_quantity_query:
            if size == 'US_Standard_Size':
                price_size_quantity = o.US_Standard_Size
            elif size == 'European_Size':
                price_size_quantity = o.European_Size
            elif size == 'Square':
                price_size_quantity = o.Square

        for y in discount_query:
            price_discount = y.Discount

        # adding sum of options        
        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + price_size_quantity)

        
        #testing
        print('----------')
        print(price_paper)
        print('----------')
        print(price_side)
        print('----------')
        print(price_size_quantity)
        print('----------')
        print(total_price)
        print('----------')
        print('-',price_discount)

        extra_f_dict = {"size": size,
                        "paper_type": paper_type,
                        "sides": sides,
                        "color": color}    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 2
        request.session['cat'] = 'bc_products'
        request.session['extra_f'] = extra_f_dict
        request.session['quantity'] = quantity
        print('Form Submitted')


    else:
        total_price = 0
        request.session['invoice'] = 0
        request.session['label'] = 0
        request.session['discount'] = 0
        print('Form Not Submitted')

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
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/edge-painted-cards.html", context)
