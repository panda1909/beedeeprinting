from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products 
from Large_Format_Printing.models import FoamcorePosters, PosterPrinting, RetractableBanners, TableCovers , FloorStickers , Extra_features
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products
from Business_Cards.models import business_cards_price

from django.http import HttpResponse
from django.template import loader


def Foamcore_poster_detail (request):
    
    product = lf_products.objects.get(id=4)
    table = FoamcorePosters.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["floor-stickers-detail", "foamcore-poster-detail", "poster-printing-detail", "retractable-banners-detail", "table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = FoamcorePosters.objects.all()
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
       
        type_quantity_query = FoamcorePosters.objects.filter(quantity=quantity)
      
        size_query = Extra_features.objects.filter(size=size).values('id','size_price')
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
        print(paper_price_query)
        if sides == 'two_sided':
            print(sides_query)
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)

        for o in size_query:
            price_size = o['size_price']
            print(price_size)

        for p in type_quantity_query:
            if printing_type == 'digital_Fast':
                price_type = p.digital_Fast
            elif printing_type == 'offset_HQ':
                price_type = p.offset_HQ

        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_size) * float(quantity)) + price_type) - price_discount

        extra_f_dict = {"printing_type": printing_type,
                        "size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'bc_products'
        request.session['extra_f'] = extra_f_dict
        request.session['quantity'] = quantity
        print('Form Submitted')
    else:
        total_price = 0
        request.session['invoice'] = 0
        request.session['label'] = ' '
        request.session['discount'] = 0
        request.session['id'] = 1
        request.session['quantity'] = 0
        request.session['cat'] = 'bc_products'
        print('Form not submitted')



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
        "bc_aside"   : bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside" : lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render(request, "Large_Format_Printing/foamcore_posters.html", context)

def Poster_printing_detail(request):
        
    product = lf_products.objects.get(id=5)
    table = PosterPrinting.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["floor-stickers-detail", "foamcore-poster-detail", "poster-printing-detail", "retractable-banners-detail", "table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    menu = PosterPrinting.objects.all()
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
       
        type_quantity_query = PosterPrinting.objects.filter(quantity=quantity)
      
        size_query = Extra_features.objects.filter(size=size).values('id','size_price')
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
        print(paper_price_query)
        if sides == 'two_sided':
            print(sides_query)
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)

        for o in size_query:
            price_size = o['size_price']
            print(price_size)

        for p in type_quantity_query:
            if printing_type == 'digital_Fast':
                price_type = p.digital_Fast
            elif printing_type == 'offset_HQ':
                price_type = p.offset_HQ

        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_size) * float(quantity)) + price_type) - price_discount

        extra_f_dict = {"printing_type": printing_type,
                        "size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'bc_products'
        request.session['extra_f'] = extra_f_dict
        request.session['quantity'] = quantity
        print('Form Submitted')
    else:
        total_price = 0
        request.session['invoice'] = 0
        request.session['label'] = ' '
        request.session['discount'] = 0
        request.session['id'] = 1
        request.session['quantity'] = 0
        request.session['cat'] = 'bc_products'
        print('Form not submitted')



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
        "bc_aside"   : bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside" : lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render( request,"Large_Format_Printing/poster_printing.html", context )

def Retractable_banners_detail(request):
        
    product = lf_products.objects.get(id=7)
    table = RetractableBanners.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["floor-stickers-detail", "foamcore-poster-detail", "poster-printing-detail", "retractable-banners-detail", "table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    menu = RetractableBanners.objects.all()
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
       
        type_quantity_query = RetractableBanners.objects.filter(quantity=quantity)
      
        size_query = Extra_features.objects.filter(size=size).values('id','size_price')
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
        print(paper_price_query)
        if sides == 'two_sided':
            print(sides_query)
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)

        for o in size_query:
            price_size = o['size_price']
            print(price_size)

        for p in type_quantity_query:
            if printing_type == 'digital_Fast':
                price_type = p.digital_Fast
            elif printing_type == 'offset_HQ':
                price_type = p.offset_HQ

        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_size) * float(quantity)) + price_type) - price_discount

        extra_f_dict = {"printing_type": printing_type,
                        "size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'bc_products'
        request.session['extra_f'] = extra_f_dict
        request.session['quantity'] = quantity
        print('Form Submitted')
    else:
        total_price = 0
        request.session['invoice'] = 0
        request.session['label'] = ' '
        request.session['discount'] = 0
        request.session['id'] = 1
        request.session['quantity'] = 0
        request.session['cat'] = 'bc_products'
        print('Form not submitted')



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
        "bc_aside"   : bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside" : lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render( request,"Large_Format_Printing/retractable_banners.html", context )




def Table_covers_detail(request):
        
    product = lf_products.objects.get(id=8)
    table = TableCovers.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["floor-stickers-detail", "foamcore-poster-detail", "poster-printing-detail", "retractable-banners-detail", "table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    menu = TableCovers.objects.all()
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
       
        type_quantity_query = TableCovers.objects.filter(quantity=quantity)
      
        size_query = Extra_features.objects.filter(size=size).values('id','size_price')
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
        print(paper_price_query)
        if sides == 'two_sided':
            print(sides_query)
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)

        for o in size_query:
            price_size = o['size_price']
            print(price_size)

        for p in type_quantity_query:
            if printing_type == 'digital_Fast':
                price_type = p.digital_Fast
            elif printing_type == 'offset_HQ':
                price_type = p.offset_HQ

        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_size) * float(quantity)) + price_type) - price_discount

        extra_f_dict = {"printing_type": printing_type,
                        "size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'bc_products'
        request.session['extra_f'] = extra_f_dict
        request.session['quantity'] = quantity
        print('Form Submitted')
    else:
        total_price = 0
        request.session['invoice'] = 0
        request.session['label'] = ' '
        request.session['discount'] = 0
        request.session['id'] = 1
        request.session['quantity'] = 0
        request.session['cat'] = 'bc_products'
        print('Form not submitted')



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
        "bc_aside"   : bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside" : lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render( request,"Large_Format_Printing/table_covers.html", context )

def Floor_stickers_detail(request):
        
    product = lf_products.objects.get(id=3)
    table = FloorStickers.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["floor-stickers-detail", "foamcore-poster-detail", "poster-printing-detail", "retractable-banners-detail", "table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    
    menu = FloorStickers.objects.all()
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
       
        type_quantity_query = FloorStickers.objects.filter(quantity=quantity)
      
        size_query = Extra_features.objects.filter(size=size).values('id','size_price')
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
        print(paper_price_query)
        if sides == 'two_sided':
            print(sides_query)
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)

        for o in size_query:
            price_size = o['size_price']
            print(price_size)

        for p in type_quantity_query:
            if printing_type == 'digital_Fast':
                price_type = p.digital_Fast
            elif printing_type == 'offset_HQ':
                price_type = p.offset_HQ

        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_size) * float(quantity)) + price_type) - price_discount

        extra_f_dict = {"printing_type": printing_type,
                        "size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'bc_products'
        request.session['extra_f'] = extra_f_dict
        request.session['quantity'] = quantity
        print('Form Submitted')
    else:
        total_price = 0
        request.session['invoice'] = 0
        request.session['label'] = ' '
        request.session['discount'] = 0
        request.session['id'] = 1
        request.session['quantity'] = 0
        request.session['cat'] = 'bc_products'
        print('Form not submitted')



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
        "bc_aside"   : bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside" : lf_aside,
        "mp_aside": mp_aside,

    }
    if request.POST:
        return redirect('checkout')
    return render( request,"Large_Format_Printing/floor_stickers.html", context )