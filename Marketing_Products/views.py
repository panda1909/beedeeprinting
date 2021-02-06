from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
# All category products
from Business_Cards.models import Products as bc_products 
from Marketing_Products.models import Calendars, BrochuresAndFlyers, PostCards, HangTags, LabelsAndStickers, NCRForms, PresentationFolders, CustomHolidayCards, Extra_features
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products
from Business_Cards.models import business_cards_price

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Calendars_detail (request):
    
    product = mp_products.objects.get(id=2)
    table = Calendars.objects.all() 
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    menu = Calendars.objects.all()
    menu1 = Extra_features.objects.all()
    
    # if stament for getting info from template

    if request.POST:
        var = request.POST
        quantity = var['quantity']
        size = var['size']
       
        size_quantity_query = Calendars.objects.filter(quantity=quantity).values('price')

        discount_query = Calendars.objects.filter(quantity=quantity).values('Discount')

        for u in size_quantity_query:
            size_quantity = u['price']

        for y in discount_query:
            price_discount = y['Discount']


        total_price = size_quantity - price_discount

        extra_f_dict = {"Size": size,
                       }

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 2
        request.session['cat'] = 'mp_products'
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
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/calenders.html", context)



def Broucher_Flyers_Detail(request):

    product = mp_products.objects.get(id=3)
    table = BrochuresAndFlyers.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)

    menu = BrochuresAndFlyers.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        var = request.POST

        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
        fold = var['fold']

        size_quantity_query = BrochuresAndFlyers.objects.filter(quantity=quantity).values('price')
        paper_type_query = Extra_features.objects.filter(paper_type=paper_type).values('paper_type_price')
        fold_query = Extra_features.objects.filter(paper_type=paper_type).values(fold)
        discount_query = BrochuresAndFlyers.objects.filter(quantity=quantity).values('Discount')
        fold_query = Extra_features.objects.filter(paper_type=paper_type).values(fold)
       
        if sides == 'two_sided':
            sides_query = Extra_features.objects.filter(paper_type=paper_type).values('second_side_printing_price')
            for u in sides_query:
                price_side = u['second_side_printing_price']
                break
        else:
            price_side = 0

        for r in size_quantity_query:
            size_quantity_price = r['price']

        for i in paper_type_query:
            price_paper = i['paper_type_price']
        
        for y in discount_query:
            price_discount = y['Discount']

        for w in fold_query:
            price_fold = w[fold]


        total_price = ((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + (float(price_fold) * float(quantity)) + size_quantity_price) - price_discount

        extra_f_dict = {"Fold": fold,
                        "Size": size,
                        "paper_type": paper_type,
                        "sides": sides}

        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 3
        request.session['cat'] = 'mp_products'
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
        request.session['cat'] = 'mp_products'
        print('Form not submitted')

        #testing
        # print('----------')
        # print(price_paper)
        # print('----------')
        # print(price_side)
        # print('----------')
        # print(price_size_quantity)
        # print('----------')
        print(total_price)
        print('----------')
        # print('-',price_discount)

        # extra_f_dict = {"size": size,
                        # "paper_type": paper_type,
                        # "sides": sides,
                        # "color": color}    
    
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
    return render(request, "Marketing_Products/brouchers&flyers.html", context)


def Postcard_Detail (request):

    product = mp_products.objects.get(id=1)
    table = PostCards.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)    
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = PostCards.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        paper_type = request.POST.get('paper_type')
        sides = request.POST.get('sides')
        coating = request.POST.get('coating')

        size_quantity_query = PostCards.objects.filter(Quantity=quantity).values(size)
       
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('paper_type_price')

        discount_query = PostCards.objects.filter(Quantity=quantity).values('Discount')

        # sides price query
        if sides == 'two_sided':
            sides_query = Extra_features.objects.filter(paper_type=paper_type).values('second_side_printing_price')
            print(sides_query)
            for u in sides_query:
                price_side = u['second_side_printing_price']
                break
        else:
            price_side = 0

        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in size_quantity_query:
            price_size_quantity = o[size]
            
        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = (((float(price_paper) * float(quantity)) + (float(price_side) * float(quantity)) + price_size_quantity)) - price_discount

        extra_f_dict = {"Size": size,
                        "Paper_type": paper_type,
                        "Sides": sides,
                        "Coating": coating,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 1
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/postcards.html", context)


def Hangtags_Detail (request):

    product = mp_products.objects.get(id=4)
    table = HangTags.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)    
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = HangTags.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']

        # queries against relevant options
        # size and quantity price query
        size_quantity_query = HangTags.objects.filter(Quantity=quantity).values(size)
       
        # paper type price query
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('paper_type_price')

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = HangTags.objects.filter(Quantity=quantity).values('Discount')



        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in size_quantity_query:
            price_size_quantity = o[size]

        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = ((float(price_paper) * float(quantity)) + price_size_quantity) - price_discount

        extra_f_dict = {"Size": size,
                        "Paper_type": paper_type,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 4
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/hangtags.html", context)

def Laberlsandstickers_Detail(request):

    product = mp_products.objects.get(id=5)
    table = LabelsAndStickers.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    bc_aside = zip(urls_bc_aside,bc_object)
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)    
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = LabelsAndStickers.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        shape = var['shape']
        format = var['format']

        # queries against relevant options
        # size and quantity price query
        size_quantity_query = LabelsAndStickers.objects.filter(Quantity=quantity).values(size)
       
        # format type price query
        if format == 'individual_cut_labels_price':
            format_price_query = Extra_features.objects.values_list('individual_cut_labels_price', flat=True)
            price_format = format_price_query[0]
        else:
            price_format = 0
                

        # Discount query
        discount_query = LabelsAndStickers.objects.filter(Quantity=quantity).values('Discount')

        for u in size_quantity_query:
            price_size_quantity = u[size]

        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = ((float(price_format) * float(quantity)) + price_size_quantity) - price_discount

        extra_f_dict = {"Size": size,
                        "Shape": shape,
                        "Roll or Individually Cut": format,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 5
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/labelsnstickers.html", context)

def NCRforms_Detail (request):

    product = mp_products.objects.get(id=6)
    table = NCRForms.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = NCRForms.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        number = var['number']
        parts = var['parts']
        color = var['color']

        # queries against relevant options
        # size and quantity price query
        size_quantity_query = NCRForms.objects.filter(Quantity=quantity).values(size)
       
        # numbered price query
        if number == 'form_numbering_price':
            number_price_query = Extra_features.objects.values(number)
            for t in number_price_query:
                price_number = t[number]
                break
        else:
            price_number = 0 

        # 3 part NCR query
        if parts == 'three_part_form_price':
            part_price_query = Extra_features.objects.values(parts)
            for r in part_price_query:
                price_parts = r[parts]
                break
        else:
            price_parts = 0

        # Discount query
        discount_query = NCRForms.objects.filter(Quantity=quantity).values('Discount')


        for o in size_quantity_query:
            price_size_quantity = o[size]
            
        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = ((float(price_parts) * float(quantity)) + (float(price_number) * float(quantity)) + price_size_quantity) - price_discount


        extra_f_dict = {"Size": size,
                        "Form Numbering": number,
                        "Parts": parts,
                        "Color": color}    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 6
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/ncrforms.html", context)

def Presentation_folder_Detail (request):

    product = mp_products.objects.get(id=7)
    table = PresentationFolders.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = PresentationFolders.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        paper_type = var['paper_type']
        sides = var['sides']
        coating = var['coating']
        pockets = var['pockets']
        slits = var['slits']

        ### queries against relevant options ###
        
        # size and quantity price query
        size_quantity_query = PresentationFolders.objects.filter(Quantity=quantity).values(size)

        # paper type price query
        paper_price_query = Extra_features.objects.filter(paper_type=paper_type).values('paper_type_price')

        # Discount query
        discount_query = PresentationFolders.objects.filter(Quantity=quantity).values('id', 'Discount')


        for i in paper_price_query:
            price_paper = i['paper_type_price']

        for o in size_quantity_query:
            price_size_quantity = o[size]

        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = ((float(price_paper) * float(quantity)) + price_size_quantity) - price_discount

        
        extra_f_dict = {"Size": size,
                        "paper_type": paper_type,
                        "sides": sides,
                        "coating": coating,
                        "pockets": pockets,
                        "slits": slits,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 7
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/presentation_folders.html", context)


def Custom_holiday_cards_Detail (request):

    product = mp_products.objects.get(id=8)
    table = CustomHolidayCards.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc_aside =  urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    urls_mp_aside = ["calenders-detail","brouchers-flyers-detail" , "postcards-detail", "hangtags-detail", "labels-and-stickers-detail" , "ncr-forms-detail" , "presentation-folder-detail", "custom-holiday-cards-detail"]
    mp_aside = zip(urls_mp_aside, mp_object)
    bs_aside = zip(urls_bs_aside, bs_object)
    bc_aside = zip(urls_bc_aside,bc_object)
    lf_aside = zip(urls_lf_aside, lf_object)
    menu = CustomHolidayCards.objects.all()
    menu1 = Extra_features.objects.all()

    # if stament for getting info from template

    if request.POST:
        # assigning user selected option to variable for queries
        var = request.POST
        quantity = var['quantity']
        size = var['size']
        sides = var['sides']
        blank_envelope = var['blank_envelope']

        # queries against relevant options
        # size and quantity price query
        size_quantity_query = CustomHolidayCards.objects.filter(Quantity=quantity).values(size)
       
        # paper type price query
        if blank_envelope == 'blank_envelope_price':
            envelope_price_query = Extra_features.objects.values(blank_envelope)
            for u in envelope_price_query:
                price_envelope = u[blank_envelope]
                break
        else:
            price_envelope = 0

        # Discount query
        # discount_query = edge_painted_business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_edge_painted_business_cards_price WHERE quantity = %s', [quantity])
        discount_query = CustomHolidayCards.objects.filter(Quantity=quantity).values('Discount')


        for o in size_quantity_query:
            price_size_quantity = o[size]

        for y in discount_query:
            price_discount = y['Discount']

        # adding sum of options        
        total_price = ((float(price_envelope) * float(quantity)) + price_size_quantity) - price_discount


        extra_f_dict = {"Size": size,
                        "Sides": sides,
                        "Blank Envelope": blank_envelope,
                        }    
    
        request.session['invoice'] = total_price
        request.session['label'] = product.Label
        request.session['discount'] = price_discount
        request.session['id'] = 8
        request.session['cat'] = 'mp_products'
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
    return render(request, "Marketing_Products/custom_holiday_cards.html", context)