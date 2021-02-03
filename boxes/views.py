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

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
    
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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

def Gable_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/gable_box.html', context)

def Windows_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/window_box.html', context)

def Mailer_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/mailer_box.html', context)

def Kraft_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/kraft_box.html', context)

def Cosmetics_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]
    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/cosmetics_box.html', context)

def Display_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]
    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/display_box.html', context)

def Sleeve_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/sleeve_box.html', context)

def Beverages_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/beverage_box.html', context)

def Candle_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/candle_box.html', context)

def Autoparts_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/auto_parts_box.html', context)

def Pizza_Boxes(request):
    product = b_products.objects.get(id=1)
    
    b_object = b_products.objects.all()
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()

    urls_bc_aside = ["/business-cards/business-card-detail" , "/business-cards/edge-painted-detail", "/business-cards/foil-business-card-detail","/business-cards/raised-spot-uv-business-card-detail", "/business-cards/pantone-business-cards-detail", "/business-cards/plastic-business-cards-detail", "/business-cards/raised-ink-business-cards-detail"]
    
    urls_bs_aside =  ["/business-stationary/envelopes-detail", "/business-stationary/letterhead-detail", "/business-stationary/notepad-detail"]
    
    urls_lf_aside = ["/large-format/floor-stickers-detail", "/large-format/foamcore-poster-detail", "/large-format/poster-printing-detail", "/large-format/retractable-banners-detail", "/large-format/table-cover-detail"]
    
    urls_mp_aside = ["/marketing-products/calenders-detail", "/marketing-products/brouchers-flyers-detail" , "/marketing-products/postcards-detail", "/marketing-products/hangtags-detail", "/marketing-products/labels-and-stickers-detail" , "/marketing-products/ncr-forms-detail" , "/marketing-products/presentation-folder-detail", "custom-holiday-cards-detail"]
   
    b_urls = ["pillow-boxes-detail", "gable-boxes-detail" ," window-boxes-detail", "mailer-boxes-detail" , " kraft-boxes-detail", "cosmetics-boxes-detail" ,"display-boxes-detail", "sleeve-boxes-detail", "beverage-boxes-detail", "candle-boxes-detail", "auto-parts-boxes-detail", "pizza-boxes-detail"]

    bc_aside = zip(urls_bc_aside,bc_object)
    bs_aside = zip(urls_bs_aside,bs_object)
    lf_aside = zip(urls_lf_aside,lf_object)
    mp_aside = zip(urls_mp_aside,mp_object)
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


    return render(request, 'boxes/ppizza_box.html', context)

