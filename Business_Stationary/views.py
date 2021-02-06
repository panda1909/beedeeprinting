from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products 
from Business_Stationary.models import Envelopes, LetterHeads, NotePads, Extra_features
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products
from Business_Cards.models import business_cards_price
from boxes.models import Products as b_products

from django.http import HttpResponse
from django.template import loader


def Envelops_detail (request):
    
    product = bs_products.objects.get(id=1)
    table = Envelopes.objects.all() 
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["envelopes-detail", "letterhead-detail", "notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    b_urls = ["/boxes/pillow-boxes-detail", "/boxes/gable-boxes-detail" ,"/boxes/window-boxes-detail", "/boxes/mailer-boxes-detail" , "/boxes/kraft-boxes-detail", "/boxes/cosmetics-boxes-detail" ,"/boxes/sleeve-boxes-detail", "/boxes/display-boxes-detail", "/boxes/beverage-boxes-detail", "/boxes/candle-boxes-detail", "/boxes/auto-parts-boxes-detail", "/boxes/pizza-boxes-detail"]

    b_aside = zip(b_urls,b_object)
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    menu = Envelopes.objects.all()
    menu1 = Extra_features.objects.all()
    
    # if stament for getting info from template

    if request.POST:
        var = request.POST

        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
        window = var['window']
       
        if size == 'Number_10':
            size_quantity_query = Envelopes.objects.filter(Quantity=quantity).values('Number_10')
        elif size == 'Nine_By_Twleve':
            size_quantity_query = Envelopes.objects.filter(Quantity=quantity).values('Nine_By_Twleve')
        elif size == 'A7':
            size_quantity_query = Envelopes.objects.filter(Quantity=quantity).values('A7')

        for r in size_quantity_query:
            price_type = r[size]

        discount_query = Envelopes.objects.filter(Quantity=quantity).values('Discount')
        
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
 
        if sides == 'two_sided':
            sides_query = Extra_features.objects.filter(paper_type=paper_type).values('second_side_price')
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        if window == 'standard_window':
            window_query = Extra_features.objects.filter(paper_type=paper_type).values('standard_window_price') 
            for t in window_query:
                price_window = t['standard_window_price']
                break   
        else:
            price_window = 0


        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)


        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + price_type) - price_discount

        extra_f_dict = {"Window": window,
                        "Size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'bs_products'
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
        "lf_aside": lf_aside, 
        "b_aside": b_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render(request, "Business_Stationary/envelopes.html", context)

def Letterhead_detail(request):
        
    product = bs_products.objects.get(id=2)
    table = LetterHeads.objects.all() 
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["envelopes-detail", "letterhead-detail", "notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    b_urls = ["/boxes/pillow-boxes-detail", "/boxes/gable-boxes-detail" ,"/boxes/window-boxes-detail", "/boxes/mailer-boxes-detail" , "/boxes/kraft-boxes-detail", "/boxes/cosmetics-boxes-detail" ,"/boxes/sleeve-boxes-detail", "/boxes/display-boxes-detail", "/boxes/beverage-boxes-detail", "/boxes/candle-boxes-detail", "/boxes/auto-parts-boxes-detail", "/boxes/pizza-boxes-detail"]

    b_aside = zip(b_urls,b_object)
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    menu = LetterHeads.objects.all()
    menu1 = Extra_features.objects.all()
    
    # if stament for getting info from template

    if request.POST:
        var = request.POST
        #print(var)
        #print('---------')
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
       
        size_quantity_query = LetterHeads.objects.filter(Quantity=quantity).values('Eight_By_Five_By_Eleven')

        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('paper_type_price')

        discount_query = LetterHeads.objects.filter(Quantity=quantity).values('Discount')

        print(paper_price_query)
        if sides == 'two_sided':
            sides_query = Extra_features.objects.filter(paper_type=paper_type).values('second_side_price')
            for u in sides_query:
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']
            print(price_paper)

        for o in size_quantity_query:
            price_size_quantity = o['Eight_By_Five_By_Eleven']
            

        for y in discount_query:
            price_discount = y['Discount']


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + price_size_quantity) - price_discount

        extra_f_dict = {"Size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 2
        request.session['cat'] = 'bs_products'
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
        "lf_aside": lf_aside, 
        "b_aside": b_aside,
        "mp_aside": mp_aside,

    }
    if request.POST:
        return redirect('checkout')
    return render( request, "Business_Stationary/letterhead.html", context )

def Notepad_detail(request):
        
    product = bs_products.objects.get(id=3)
    table = NotePads.objects.all() 
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["envelopes-detail", "letterhead-detail", "notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    b_urls = ["/boxes/pillow-boxes-detail", "/boxes/gable-boxes-detail" ,"/boxes/window-boxes-detail", "/boxes/mailer-boxes-detail" , "/boxes/kraft-boxes-detail", "/boxes/cosmetics-boxes-detail" ,"/boxes/sleeve-boxes-detail", "/boxes/display-boxes-detail", "/boxes/beverage-boxes-detail", "/boxes/candle-boxes-detail", "/boxes/auto-parts-boxes-detail", "/boxes/pizza-boxes-detail"]

    b_aside = zip(b_urls,b_object)
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    menu = NotePads.objects.all()
    menu1 = Extra_features.objects.all()
    
    # if stament for getting info from template

    if request.POST:
        var = request.POST
        #print(var)
        #print('---------')
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
       
        size_quantity_query = NotePads.objects.filter(Quantity=quantity).values('Three_By_Six_By_Four_By_Eight')
      
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')

        discount_query = NotePads.objects.filter(Quantity=quantity).values('Discounted')

        
        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for p in size_quantity_query:
            price_size_quantity = p['Three_By_Six_By_Four_By_Eight']
        
        for y in discount_query:
            price_discount = y['Discounted']


        total_price = ((float(price_paper) * float(quantity)) + price_size_quantity) - price_discount

        extra_f_dict = {"Size": size,
                        "paper_type": paper_type,
                        }

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 3
        request.session['cat'] = 'bs_products'
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
        "lf_aside": lf_aside, 
        "b_aside": b_aside, 
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render( request, "Business_Stationary/notepad.html", context )