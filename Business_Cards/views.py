from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products 
from Business_Cards.models import edge_painted_business_cards_price, Extra_features, foil_business_cards_price, raised_spot_uv_business_cards_price, raised_ink_business_cards_price, pantone_business_cards_price, plastic_business_cards_price
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products
from Business_Cards.models import business_cards_price

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def BC_Detail(request):
    
    product = bc_products.objects.get(id=1)
    table = business_cards_price.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail", "pantone-business-cards-detail", "plastic-business-cards-detail", "raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

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
       
        type_quantity_query = business_cards_price.objects.filter(quantity=quantity)
      
        size_query = Extra_features.objects.filter(size=size).values('id','size_price')
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id','paper_type_price')
        discount_query = business_cards_price.objects.filter(quantity=quantity).values('Discount')
        # print(paper_price_query)
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
                        "Size": size,
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
        "lf_aside": lf_aside, 
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('checkout')
    return render(request, "Business_Cards/bc_detail.html", context)



def Edge_painted_Detail(request):

    product = bc_products.objects.get(id=2)
    table = edge_painted_business_cards_price.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail", "pantone-business-cards-detail", 'plastic-business-cards-detail', 'raised-ink-business-cards-detail']
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

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
        print(size)
        if size == 'US_Standard_Size':
            extra_size = '2"x3.5" - US Standard Size'
            type_quantity_query = edge_painted_business_cards_price.objects.filter(quantity=quantity).values('id','US_Standard_Size')
        elif size == 'European_Size':
            extra_size = '2.125"x3.375" - European Size'
            type_quantity_query = edge_painted_business_cards_price.objects.filter(quantity=quantity).values('id', 'European_Size')
        elif size == 'Square':
            extra_size = size
            type_quantity_query = edge_painted_business_cards_price.objects.filter(quantity=quantity).values('id', 'Square')

        # paper type price query
        # paper_price_query = Extra_features.objects.raw('SELECT id, paper_type_price FROM Business_Cards_Extra_features WHERE paper_type = %s', [paper_type])
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id', 'paper_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = edge_painted_business_cards_price.objects.filter(quantity=quantity).values('id', 'Discount')



        # sides price query
        if sides == 'two_sided':
            # sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            sides_query = Extra_features.objects.filter(size=extra_size).values('id', 'size', 'second_side_price')
            print(sides_query)
            for u in sides_query:
                # print('------Second Side Price--------')
                # print(u)
                price_side = u['second_side_price']
                break
        else:
            price_side = 0


        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in type_quantity_query:
            if size == 'US_Standard_Size':
                price_size_quantity = o['US_Standard_Size']
            elif size == 'European_Size':
                price_size_quantity = o['European_Size']
            elif size == 'Square':
                price_size_quantity = o['Square']

        for y in discount_query:
            price_discount = y['Discount']

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
        "bc_aside": bc_aside,
        "bs_aside" : bs_aside,
        "lf_aside": lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/edge-painted-cards.html", context)


def Foil_business_card (request):

    product = bc_products.objects.get(id=3)
    table = foil_business_cards_price.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail", "pantone-business-cards-detail", 'plastic-business-cards-detail', 'raised-ink-business-cards-detail']
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = foil_business_cards_price.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        paper_type = request.POST.get('paper_type')
        sides = request.POST.get('sides')
        foil_sides = request.POST.get('foils')
        color = request.POST.get('color')

        print(quantity,size,paper_type,sides,foil_sides,color)

        extra_size = '2"x3.5" - US Standard Size'
        type_quantity_query = foil_business_cards_price.objects.filter(quantity=quantity).values('id','price')
       
        # paper type price query
        # paper_price_query = Extra_features.objects.raw('SELECT id, paper_type_price FROM Business_Cards_Extra_features WHERE paper_type = %s', [paper_type])
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id', 'paper_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = foil_business_cards_price.objects.filter(quantity=quantity).values('id', 'Discount')



        # sides price query
        if sides == 'two_sided':
            # sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            sides_query = Extra_features.objects.filter(size=extra_size).values('id', 'size', 'second_side_price')
            print(sides_query)
            for u in sides_query:
                # print('------Second Side Price--------')
                # print(u)
                price_side = u['second_side_price']
                break
        else:
            price_side = 0

        # foil side query
        if foil_sides == 'two_sided':
            foil_sides_query = Extra_features.objects.filter(size=extra_size).values('second_side_foil_price')
            for q in foil_sides_query:
                foi_side_price = q['second_side_foil_price']



        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in type_quantity_query:
            price_size_quantity = o['price']
            
        for y in discount_query:
            price_discount = y['Discount']

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

        extra_f_dict = {"Size": size,
                        "Paper_type": paper_type,
                        "Sides": sides,
                        "Foil color": color,
                        "Foil Sides": foil_sides}    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 3
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

    print(request.session['invoice'])

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
        "bc_aside": bc_aside,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
        "bs_aside" : bs_aside,
        "lf_aside": lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/foils_bc.html", context)


def Raised_spot_uv(request):

    product = bc_products.objects.get(id=4)
    table = raised_spot_uv_business_cards_price.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail" , "pantone-business-cards-detail", 'plastic-business-cards-detail', 'raised-ink-business-cards-detail']
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = raised_spot_uv_business_cards_price.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
        raised = var['raised']

        # queries against relevant options
        # size and quantity price query
        print(size)
        if size == 'US_Standard_Size':
            extra_size = '2"x3.5" - US Standard Size'
            type_quantity_query = foil_business_cards_price.objects.filter(quantity=quantity).values('id','price')
       
        # paper type price query

        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id', 'paper_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = raised_spot_uv_business_cards_price.objects.filter(quantity=quantity).values('id', 'Discount')



        # sides price query
        if sides == 'two_sided':
            # sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            sides_query = Extra_features.objects.filter(size=extra_size).values('id', 'size', 'second_side_raied_price')
            print(sides_query)
            for u in sides_query:
                # print('------Second Side Price--------')
                # print(u)
                price_side = u['second_side_raied_price']
                break
        else:
            price_side = 0


        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in type_quantity_query:
            price_size_quantity = o['price']


        for y in discount_query:
            price_discount = y['Discount']

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

        extra_f_dict = {"Size": size,
                        "Paper_type": paper_type,
                        "Sides": sides,
                        "Raised Sides": raised,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 4
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
        "bc_aside": bc_aside,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
        "bs_aside" : bs_aside,
        "lf_aside": lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/raised_spot_uv.html", context)

def Pantone_business_cards(request):

    product = bc_products.objects.get(id=5)
    table = pantone_business_cards_price.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail", "pantone-business-cards-detail", 'plastic-business-cards-detail', 'raised-ink-business-cards-detail' ]
    bc_aside = zip(urls_bc_aside,bc_object)
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = raised_spot_uv_business_cards_price.objects.all()
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
        printing_type = var['printing_type']

        # queries against relevant options
        # size and quantity price query
        print(size)
        type_quantity_query = pantone_business_cards_price.objects.filter(quantity=quantity).values('id','price')
       
        print(type_quantity_query)

        # paper type price query
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('paper_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = pantone_business_cards_price.objects.filter(quantity=quantity).values('id', 'Discount')



        # sides price query
        if sides == 'two_sided':
            # sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            sides_query = Extra_features.objects.filter(size=extra_size).values('id', 'size', 'second_side_price')
            print(sides_query)
            for u in sides_query:
                # print('------Second Side Price--------')
                # print(u)
                price_side = u['second_side_price']
                break
        else:
            price_side = 0


        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in type_quantity_query:
            price_size_quantity = o['price']

        for y in discount_query:
            price_discount = y['Discount']

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

        extra_f_dict = {"Size": size,
                        "paper_type": paper_type,
                        "sides": sides,
                        "color": color,
                        "printing_type": printing_type,}    
        
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 5
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
        "bc_aside": bc_aside,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
        "bs_aside" : bs_aside,
        "lf_aside": lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/pantone_cards.html", context)

def Plastic_business_card (request):

    product = bc_products.objects.get(id=6)
    table = plastic_business_cards_price.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail", "pantone-business-cards-detail", 'plastic-business-cards-detail', 'raised-ink-business-cards-detail' ]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = plastic_business_cards_price.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        plastic_type = var['plastic_type']
        corner = var['corner']

        # queries against relevant options
        # size and quantity price query
        print(size)
        if size == 'US_Standard_Size':
            extra_size = '2"x3.5" - US Standard Size'
            type_quantity_query = plastic_business_cards_price.objects.filter(quantity=quantity).values('id',size)
       
        # paper type price query
        # paper_price_query = Extra_features.objects.raw('SELECT id, paper_type_price FROM Business_Cards_Extra_features WHERE paper_type = %s', [paper_type])
        plastic_price_query = Extra_features.objects.filter(plastic_type=plastic_type).values('id', 'plastic_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = plastic_business_cards_price.objects.filter(quantity=quantity).values('id', 'Discount')


        for i in plastic_price_query:
            price_plastic = i['plastic_type_price']

        for o in type_quantity_query:
            if size == 'US_Standard_Size':
                price_size_quantity = o['US_Standard_Size']
            elif size == 'Credit_card_Size':
                price_size_quantity = o['Credit_card_Size']

        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = ((float(price_plastic) * float(quantity)) + price_size_quantity)

        
        #testing
        print('----------')
        print(price_plastic)
        print('----------')
        print(price_size_quantity)
        print('----------')
        print(total_price)
        print('----------')
        print('-',price_discount)

        extra_f_dict = {"Size": size,
                        "plastic_type": plastic_type,
                        "corner": corner,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 6
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
        "bc_aside": bc_aside,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
        "bs_aside" : bs_aside,
        "lf_aside": lf_aside,
        "mp_aside": mp_aside,
    }
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/plastic_bc.html", context)

def raised_ink_business_cards (request):

    product = bc_products.objects.get(id=7)
    table = raised_ink_business_cards_price.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside = ["business-card-detail" , "edge-painted-detail", "foil-business-card-detail","raised-spot-uv-business-card-detail", "pantone-business-cards-detail", 'plastic-business-cards-detail', 'raised-ink-business-cards-detail' ]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    
    menu = raised_ink_business_cards_price.objects.all()
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
        print(size)
        if size == 'US_Standard_Size':
            extra_size = '2"x3.5" - US Standard Size'
            type_quantity_query = raised_ink_business_cards_price.objects.filter(quantity=quantity).values('id','US_Standard_Size')
       
        # paper type price query
        # paper_price_query = Extra_features.objects.raw('SELECT id, paper_type_price FROM Business_Cards_Extra_features WHERE paper_type = %s', [paper_type])
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('id', 'paper_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = raised_ink_business_cards_price.objects.filter(quantity=quantity).values('id', 'Discount')



        # sides price query
        if sides == 'two_sided':
            # sides_query = Extra_features.objects.raw('SELECT id, second_side_price FROM Business_Cards_Extra_features')
            sides_query = Extra_features.objects.filter(size=extra_size).values('id', 'size', 'second_side_price')
            print(sides_query)
            for u in sides_query:
                # print('------Second Side Price--------')
                # print(u)
                price_side = u['second_side_price']
                break
        else:
            price_side = 0


        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in type_quantity_query:
            price_size_quantity = o['US_Standard_Size']


        for y in discount_query:
            price_discount = y['Discount']

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

        extra_f_dict = {"Size": size,
                        "paper_type": paper_type,
                        "sides": sides,
                        "color": color}    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 7
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
        "bc_aside": bc_aside,
        "Description": product.Description,
        "image1" : product.image1,
        "image2" : product.image2,
        "image3" : product.image3,
        "bs_aside" : bs_aside,
        "lf_aside": lf_aside,
        "mp_aside": mp_aside,
        
    }
    if request.POST:
        return redirect('/checkout')
    return render(request, "Business_Cards/raised_ink.html", context)