from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
import json
# All category products
from Business_Cards.models import Products as bc_products 
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products
from boxes.models import Products as b_products

# order and customer table
from .models import Orders, CustomerData
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader
from .form import checkoutForm,queries, bookcalls, BoxcheckoutForm

import shortuuid
from nocasedict import NocaseDict


# Create your views here.

def Home(request):
    form = bookcalls(request.POST)
    if request.method == 'POST':
        if form.is_valid:
            form.save()

    products_search = NocaseDict({'Business Card': "business-cards/business-card-detail",'Edge Painted business card': "business-cards/edge-painted-detail",
                'Foil Business Card': "business-cards/foil-business-card-detail",'Raised spot UV business card': "business-cards/raised-spot-uv-business-card-detail",
                'Pantone Business Card':"business-cards/pantone-business-cards-detail",'Plastic Business Card': "business-cards/plastic-business-cards-detail",
                'Raised Ink Business Card':"business-cards/raised-ink-business-cards-detail",'Envelopes': "business-stationary/envelopes-detail",'Letter Head':  "business-stationary/letterhead-detail", 'Notepad': "business-stationary/notepad-detail",'Floor Stickers': "large-format/floor-stickers-detail",'Foamcore Poster': "large-format/foamcore-poster-detail",'Poster Printing': "large-format/poster-printing-detail",'Retractable Banners': "large-format/retractable-banners-detail",'Table Covers': "large-format/table-cover-detail",'Postcard': "marketing-products/postcards-detail", 'Calenders': "marketing-products/calenders-detail", 'Brouchers': "marketing-products/brouchers-flyers-detail", 'Flyers': "marketing-products/brouchers-flyers-detail",'Hangtags': "marketing-products/hangtags-detail",'Labels':"marketing-products/labels-and-stickers-detail", 'Stickers':"marketing-products/labels-and-stickers-detail",'NCR Forms': "marketing-products/ncr-forms-detail",'Presentation Folders':"marketing-products/presentation-folder-detail", 'Custom Holiday Card': "marketing-products/custom-holiday-cards-detail",'Pillow Boxes':"boxes/pillow-boxes-detail",'Gable Boxes': "boxes/gable-boxes-detail", 
                'Window Boxes': "boxes/window-boxes-detail",'Mailer Boxes': "boxes/mailer-boxes-detail",'Kraft Boxes': "boxes/kraft-boxes-detail",'Cosmetics': "boxes/cosmetics-boxes-detail",'Sleeve Boxes': "boxes/sleeve-boxes-detail",'Display Boxes': "boxes/display-boxes-detail", 'Beverages Boxes': "boxes/beverage-boxes-detail",'Candle Boxes': "boxes/candle-boxes-detail",'Auto-Parts Boxes': "boxes/auto-parts-boxes-detail",'Pizza Boxes': "boxes/pizza-boxes-detail" })
    try:    
        if request.method == 'POST':
            var = request.POST
            search_item = var['search']
            if search_item in products_search:
                return redirect(products_search[search_item])
            else:
                print("not")
    except:
        print("not")
    context = {
        'show_items': products_search.keys,
        "form": form
    }
    return render(request, "core/index.html", context)
def Search(request):
    products_search = NocaseDict({'Business Card': "business-cards/business-card-detail",'Edge Painted business card': "business-cards/edge-painted-detail",
                'Foil Business Card': "business-cards/foil-business-card-detail",'Raised spot UV business card': "business-cards/raised-spot-uv-business-card-detail",
                'Pantone Business Card':"business-cards/pantone-business-cards-detail",'Plastic Business Card': "business-cards/plastic-business-cards-detail",
                'Raised Ink Business Card':"business-cards/raised-ink-business-cards-detail",'Envelopes': "business-stationary/envelopes-detail",'Letter Head':  "business-stationary/letterhead-detail", 'Notepad': "business-stationary/notepad-detail",'Floor Stickers': "large-format/floor-stickers-detail",'Foamcore Poster': "large-format/foamcore-poster-detail",'Poster Printing': "large-format/poster-printing-detail",'Retractable Banners': "large-format/retractable-banners-detail",'Table Covers': "large-format/table-cover-detail",'Postcard': "marketing-products/postcards-detail", 'Calenders': "marketing-products/calenders-detail", 'Brouchers': "marketing-products/brouchers-flyers-detail", 'Flyers': "marketing-products/brouchers-flyers-detail",'Hangtags': "marketing-products/hangtags-detail",'Labels':"marketing-products/labels-and-stickers-detail", 'Stickers':"marketing-products/labels-and-stickers-detail",'NCR Forms': "marketing-products/ncr-forms-detail",'Presentation Folders':"marketing-products/presentation-folder-detail", 'Custom Holiday Card': "marketing-products/custom-holiday-cards-detail",'Pillow Boxes':"boxes/pillow-boxes-detail",'Gable Boxes': "boxes/gable-boxes-detail", 
                'Window Boxes': "boxes/window-boxes-detail",'Mailer Boxes': "boxes/mailer-boxes-detail",'Kraft Boxes': "boxes/kraft-boxes-detail",'Cosmetics': "boxes/cosmetics-boxes-detail",'Sleeve Boxes': "boxes/sleeve-boxes-detail",'Display Boxes': "boxes/display-boxes-detail", 'Beverages Boxes': "boxes/beverage-boxes-detail",'Candle Boxes': "boxes/candle-boxes-detail",'Auto-Parts Boxes': "boxes/auto-parts-boxes-detail",'Pizza Boxes': "boxes/pizza-boxes-detail" })
    if request.method == 'POST':
        var = request.POST
        search_item = var['search']
        if search_item in products_search:
            return redirect(products_search[search_item])
        else:
            print("not")
    return render(request, "core/index.html", {'show_items': products_search.keys})

def Emptycart(request):
    return render(request, 'core/emptycart.html')


class Aboutus(TemplateView):
    def get(self, request):
        return render(request, 'core/aboutus.html')


def Checkout(request):
    try:
        total = request.session['invoice']    
    except:
        return redirect('empty-cart')

    label = request.session['label']
    discount = request.session['discount']
    id = request.session['id']
    category = request.session['cat']
    quantity = request.session['quantity']
    extra_f_dict = request.session['extra_f']
    json_dump = json.dumps(extra_f_dict)
    json_obj = json.loads(json_dump)
    size = extra_f_dict['Size']

    if category == 'bc_products':
        product = bc_products.objects.get(id=id)
        print(category, id)
    elif category == 'bs_products':
        product = bs_products.objects.get(id=id)
        print(category, id)
    elif category == 'lf_products':
        product = lf_products.objects.get(id=id)
        print(category, id)
    elif category == 'mp_products':
        product = mp_products.objects.get(id=id)
        print(category, id)

    print(product)

    price = total
    tax = "Shipping will be calculated after order confirmation"
    # round_tax = round(tax,2)
    # tax = round_tax
    price_final = price
    order_id = shortuuid.ShortUUID().random(length=12)
    # shipping info form
    if request.method == 'POST':
       print("--------> POST")
       form = checkoutForm(request.POST , request.FILES)
    #    print (form)
       if form.is_valid():
            Name = form.cleaned_data["FirstName"]+" "+form.cleaned_data["LastName"]
            Country = form.cleaned_data["Country"]
            City = form.cleaned_data["City"]
            Region = form.cleaned_data["Region"]
            Address = form.cleaned_data["Address"]
            Email = form.cleaned_data["Email"]
            # Mobile = form.cleaned_data["Mobile"]
            Phone = form.cleaned_data["Phone"]
            Notes_Requests = form.cleaned_data["Notes_Requests"]
            TemplateOne = request.FILES.get('TemplateOne')
            TemplateTwo = request.FILES.get('TemplateTwo')
            Notes_Requests =  form.cleaned_data["Notes_Requests"]
            zipcode = form.cleaned_data["Zipcode"]

            # session for order id page
            request.session['Name'] = Name
            request.session['order_id'] = order_id
            request.session['email'] = Email

            # print(Name)
            order = Orders.objects.create(Template=TemplateOne, Second_Template=TemplateTwo ,Customer=Name, Country=Country, City=City, Region=Region, Email=Email, Delivery_address=Address, Contact = Phone, Special_requests=Notes_Requests, Zip_Code=zipcode, Extra_features=json_obj, Price=price_final, Quantity=quantity , Size=size, Product_name=label, OrderId=order_id, Status="Pending")

          
            if CustomerData.objects.filter(Email=Email).exists() :
                Customerinfo = CustomerData.objects.get(Email=Email)
                print(Customerinfo)
                Customerinfo.Orders.add(order)
            else:
                Customerinfo = CustomerData.objects.create(Name=Name, Email=Email, Cell=Phone, Country=Country, Region=Region, City=City, Zip_Code=zipcode, Address=Address)
                Customerinfo.Orders.add(order)
            print ("--------->if")
            return redirect('order')
       else:
           print ("-----> else")
    else:
        form = checkoutForm()


    context ={
        'form': form,
        'invoice': total,
        'label': label,
        'discount': discount,
        'discounted_price': price,
        'tax': tax,
        'final_price': price_final,
        'image': product.image1,
        'quantity': quantity,
    }
    return render(request, 'core/checkout.html', context)


def BoxCheckout(request):
    id = request.session['id']
    product = b_products.objects.get(id=id)
    label = product.Label
    order_id = shortuuid.ShortUUID().random(length=12)
    form = BoxcheckoutForm

    if request.method == 'POST':
        form = BoxcheckoutForm(request.POST)
        print('----------->POST')
       
        if form.is_valid():
            print('----------->Form valid')
            Name = form.cleaned_data["FirstName"]+" "+form.cleaned_data["LastName"]
            Country = form.cleaned_data["Country"]
            City = form.cleaned_data["City"]
            Region = form.cleaned_data["Region"]
            Address = form.cleaned_data["Address"]
            zipcode = form.cleaned_data["Zipcode"]
            Email = form.cleaned_data["Email"]
            Phone = form.cleaned_data["Phone"]
            Width = form.cleaned_data["Width"]
            Height = form.cleaned_data["Height"]
            Depth = form.cleaned_data["Depth"]
            Unit = form.cleaned_data["Unit"]
            Quantity = form.cleaned_data["Quantity"]
            Color = form.cleaned_data["Color"]
            Stock = form.cleaned_data["Stock"]
            Notes_Requests = form.cleaned_data["Notes_Requests"]
            Notes_Requests =  form.cleaned_data["Notes_Requests"]

            # session for order id page
            request.session['Name'] = Name
            request.session['order_id'] = order_id
            request.session['email'] = Email
            request.session['invoice'] = '1'

            extra_feature_dict ={
                'Color' : Color,
                'Stock' : Stock,
                'Width' : Width,
                'Height' : Height,
                'Depth' : Depth,
                'Unit' : Unit,
            }

            json_dump = json.dumps(extra_feature_dict)
            json_obj = json.loads(json_dump)

            order = Orders.objects.create(Customer=Name, Country=Country, City=City, Region=Region, Email=Email, Delivery_address=Address, Contact = Phone, Special_requests=Notes_Requests, Zip_Code=zipcode, Extra_features=json_obj, Product_name=label, Quantity=Quantity, OrderId=order_id, Status="Pending")

          
            if CustomerData.objects.filter(Email=Email).exists() :
                Customerinfo = CustomerData.objects.get(Email=Email)
                print(Customerinfo)
                Customerinfo.Orders.add(order)
            else:
                Customerinfo = CustomerData.objects.create(Name=Name, Email=Email, Cell=Phone, Country=Country, Region=Region, City=City, Zip_Code=zipcode, Address=Address)
                Customerinfo.Orders.add(order)

            return redirect('order')

        else:
            print('-----------> Invalid Form')
            

    context ={
    'form': form,
    'label': label,
    'image': product.image1,
    }
    return render(request, 'core/box-checkout.html', context)


def Order_placed(request):
    label = request.session['label']
    Name = request.session['Name']
    email = request.session['email']
    order_id = request.session['order_id'] 
    subject = "Order ID"
    final_message= "Hello, "+ Name + "\n"+ "Your Order Id:"+" "+order_id + "\n For product: "+ label 
    if request.POST:
        print('request.POST')
        send_mail(
                subject,
                final_message,
                'beedee.printing@gmail.com',
                [email],
                fail_silently=True
            )
        print('order_plced view working')
        return redirect('home')
    context = {
        'Name' : Name,
        'order_id' : order_id,
        'successful_submit': True,
    }
    try:
        request.session['invoice']
    except:
        return redirect('home')
    del request.session['invoice']

    return render(request, 'core/order_placed.html', context)


def get_status(request):
    status = "Please Enter ID first."
    if request.POST:
        form = request.POST
        Order_id = form['Order_id']
        print("---------->>>>", Order_id)
        # status_query = Orders.objects.raw("SELECT id, Status FROM core_Orders WHERE OrderId = %s",[Order_id])
        status_query = Orders.objects.filter(OrderId=Order_id).values('Status')
        for p in status_query:
            status = p['Status']
    context={
        'status' : status,
    }
    return render(request, 'core/get_status.html', context)


def Cart(request):
    return render(request, 'core/cart.html')


def Contactus(request):
    form = queries(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            # save the form data to model
            var = request.POST
            message = var['Message']
            name = var['Name']
            final_message = "Hello," + name + "\n"+ message
            email = var['Email']
            subject = var['Subject']
            check = var['Contacted']
            form.save()
            if check == 'on':
                send_mail(
                subject,
                final_message,
                'beedee.printing@gmail.com',
                [email, 'bilalahmaddurrani707@gmail.com'],
                fail_silently=True
            )
    context = {
        "form": form
    }
    return render(request, 'core/contactus.html', context)

# ------  All Products page/funct  ------ #

def All_products(request):
    bc_object = bc_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    bs_object_aside = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    lf_object_aside = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    mp_object_aside = mp_products.objects.all()
    b_object = b_products.objects.all()
    b_object_aside = b_products.objects.all()
    ### urls list for BC products ###
    urls_bc = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### urls list for navbar BC products ###
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### Business Cards zip objects ###
    bc_list = zip(urls_bc,bc_object)
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    ### Urls list for BS products ###
    urls_bs = ["business-stationary/envelopes-detail","business-stationary/letterhead-detail",
                "business-stationary/notepad-detail"]
    ### Urls list for navbar BS products ###
    urls_bs_aside = ["business-stationary/envelopes-detail","business-stationary/letterhead-detail",
                    "business-stationary/notepad-detail"]
    ### Business Staionary zip objects ###
    bs_list = zip(urls_bs,bs_object)
    bs_list_aside = zip(urls_bs_aside,bs_object_aside)
    ### Urls list for lf products ###
    urls_lf = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### Urls list for navbar lf products ###
    urls_lf_aside = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### LF prodcuts zip objects ###
    lf_list = zip(urls_lf,lf_object)
    lf_list_aside = zip(urls_lf_aside,lf_object_aside)
    ### Urls list for Marketing prodcuts ###
    urls_mp = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### Urls list for navbar mp products ###
    urls_mp_aside = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### LF prodcuts zip objects ###
    mp_list = zip(urls_mp,mp_object)
    mp_list_aside = zip(urls_mp_aside,mp_object_aside)
    ### Urls list for Boxes prducts ###
    urls_b = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Urls list navbar Boxes prodcuts ###
    urls_b_aside = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Boxes Zip objects ###
    b_list = zip(urls_b,b_object)
    b_list_aside = zip(urls_b_aside, b_object_aside)

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "b_product"  : b_object,
        "bc_list"    : bc_list,
        "bc_aside"   : bc_aside,
        "bs_list"    : bs_list,
        "bs_list_aside" :  bs_list_aside,
        "lf_list"    : lf_list,
        "lf_list_aside" : lf_list_aside,
        "mp_list"    : mp_list,
        "mp_list_aside" : mp_list_aside,
        "b_list"     : b_list,
        "b_list_aside": b_list_aside,
    }
    return render(request, "core/all_products.html", context)

# ------  Catogirze Pages in frontend  ------ #
# ------  All pages are dynamic using if else and db ------ #

def Business_card(request):
    bc_card = 1
    bs_card = 0
    lf_card = 0
    mp_card = 0
    b_card = 0

    bc_object = bc_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bs_object_aside = bs_products.objects.all()
    lf_object_aside = lf_products.objects.all()
    mp_object_aside = mp_products.objects.all()
    b_object_aside = b_products.objects.all()
    ### urls list for BC products ###
    urls_bc = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### urls list for navbar BC products ###
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### Business Cards zip objects ###
    bc_list = zip(urls_bc,bc_object)
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    ### Urls list for navbar BS products ###
    urls_bs_aside = ["business-stationary/envelopes-detail" , "business-stationary/letterhead-detail" , 
                     "business-stationary/notepad-detail"]
    ### Business Staionary zip objects ###
    bs_list_aside = zip(urls_bs_aside,bs_object_aside)
    ### Urls list for navbar lf products ###
    urls_lf_aside = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### LF prodcuts zip objects ###
    lf_list_aside = zip(urls_lf_aside,lf_object_aside)
    ### Urls list for navbar mp products ###
    urls_mp_aside = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### LF prodcuts zip objects ###
    mp_list_aside = zip(urls_mp_aside,mp_object_aside)
    ### Urls list navbar Boxes prodcuts ###
    urls_b_aside = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Boxes Zip objects ###
    b_list_aside = zip(urls_b_aside, b_object_aside)

    context = {
        "bc_list" : bc_list,
        "bc_list_aside" : bc_aside,
        "bs_list_aside" : bs_list_aside,
        "lf_list_aside" : lf_list_aside,
        "mp_list_aside" : mp_list_aside,
        "b_list_aside"  : b_list_aside,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
        "b_card"  : b_card,
    }
    return render(request, "core/catogery.html", context)

def Business_stationary(request):
    bc_card = 0
    bs_card = 1
    lf_card = 0
    mp_card = 0
    b_card = 0

    bs_object = bs_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bs_object_aside = bs_products.objects.all()
    lf_object_aside = lf_products.objects.all()
    mp_object_aside = mp_products.objects.all()
    b_object_aside = b_products.objects.all()


    ### urls list for sidebar BC products ###
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### Business Cards zip objects ###
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    ### Urls list for BS products ###
    urls_bs = ["business-stationary/envelopes-detail" , "business-stationary/letterhead-detail" , 
               "business-stationary/notepad-detail"]
    ### Urls list for navbar BS products ###
    urls_bs_aside = ["business-stationary/envelopes-detail" , "business-stationary/letterhead-detail" , 
                     "business-stationary/notepad-detail"]
    ### Business Staionary zip objects ###
    bs_list = zip(urls_bs,bs_object)
    bs_list_aside = zip(urls_bs_aside,bs_object_aside)
    ### Urls list for navbar lf products ###
    urls_lf_aside = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### LF prodcuts zip objects ###
    lf_list_aside = zip(urls_lf_aside,lf_object_aside)
    ### Urls list for navbar mp products ###
    urls_mp_aside = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### LF prodcuts zip objects ###
    mp_list_aside = zip(urls_mp_aside,mp_object_aside)
    ### Urls list navbar Boxes prodcuts ###
    urls_b_aside = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Boxes Zip objects ###
    b_list_aside = zip(urls_b_aside, b_object_aside)

    context = {
        "bs_list" : bs_list,
        "bc_list_aside" : bc_aside,
        "bs_list_aside" : bs_list_aside,
        "lf_list_aside" : lf_list_aside,
        "mp_list_aside" : mp_list_aside,
        "b_list_aside"  : b_list_aside,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
        "b_card"  : b_card,
    }
    return render(request, "core/catogery.html", context)

def Large_format(request):
    bc_card = 0
    bs_card = 0
    lf_card = 1
    mp_card = 0
    b_card = 0

    lf_object = lf_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bs_object_aside = bs_products.objects.all()
    lf_object_aside = lf_products.objects.all()
    mp_object_aside = mp_products.objects.all()
    b_object_aside = b_products.objects.all()


    ### urls list for sidebar BC products ###
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### Business Cards zip objects ###
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    ### Urls list for navbar BS products ###
    urls_bs_aside = ["business-stationary/envelopes-detail" , "business-stationary/letterhead-detail" , 
                     "business-stationary/notepad-detail"]
    ### Business Staionary zip objects ###
    bs_list_aside = zip(urls_bs_aside,bs_object_aside)
    ### Urls list for lf products ###
    urls_lf = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### Urls list for navbar lf products ###
    urls_lf_aside = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### LF prodcuts zip objects ###
    lf_list = zip(urls_lf,lf_object)
    lf_list_aside = zip(urls_lf_aside,lf_object_aside)
    ### Urls list for navbar mp products ###
    urls_mp_aside = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### LF prodcuts zip objects ###
    mp_list_aside = zip(urls_mp_aside,mp_object_aside)
    ### Urls list navbar Boxes prodcuts ###
    urls_b_aside = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Boxes Zip objects ###
    b_list_aside = zip(urls_b_aside, b_object_aside)

    context = {
        "lf_list" : lf_list,
        "bc_list_aside" : bc_aside,
        "bs_list_aside" : bs_list_aside,
        "lf_list_aside" : lf_list_aside,
        "mp_list_aside" : mp_list_aside,
        "b_list_aside"  : b_list_aside,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
        "b_card"  : b_card,
    }
    return render(request, "core/catogery.html", context)

def Marketing_products(request):

    bc_card = 0
    bs_card = 0
    lf_card = 0
    mp_card = 1
    b_card = 0

    mp_object = mp_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bs_object_aside = bs_products.objects.all()
    lf_object_aside = lf_products.objects.all()
    mp_object_aside = mp_products.objects.all()
    b_object_aside = b_products.objects.all()


    ### urls list for sidebar BC products ###
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### Business Cards zip objects ###
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    ### Urls list for navbar BS products ###
    urls_bs_aside = ["business-stationary/envelopes-detail" , "business-stationary/letterhead-detail" , 
                     "business-stationary/notepad-detail"]
    ### Business Staionary zip objects ###
    bs_list_aside = zip(urls_bs_aside,bs_object_aside)
    ### Urls list for navbar lf products ###
    urls_lf_aside = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### LF prodcuts zip objects ###
    lf_list_aside = zip(urls_lf_aside,lf_object_aside)
    ### Urls list for mp products ###
    urls_mp = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### Urls list for navbar mp products ###
    urls_mp_aside = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### LF prodcuts zip objects ###
    mp_list = zip(urls_mp,mp_object)
    mp_list_aside = zip(urls_mp_aside,mp_object_aside)
    ### Urls list navbar Boxes prodcuts ###
    urls_b_aside = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Boxes Zip objects ###
    b_list_aside = zip(urls_b_aside, b_object_aside)

    context = {
        "mp_list" : mp_list,
        "bc_list_aside" : bc_aside,
        "bs_list_aside" : bs_list_aside,
        "lf_list_aside" : lf_list_aside,
        "mp_list_aside" : mp_list_aside,
        "b_list_aside"  : b_list_aside,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
        "b_card"  : b_card,
    }
    return render(request, "core/catogery.html", context)


def Packaging_products(request):
    bc_card = 0
    bs_card = 0
    lf_card = 0
    mp_card = 0
    b_card = 1

    b_object = b_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bs_object_aside = bs_products.objects.all()
    lf_object_aside = lf_products.objects.all()
    mp_object_aside = mp_products.objects.all()
    b_object_aside = b_products.objects.all()


    ### urls list for sidebar BC products ###
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail",
                "business-cards/foil-business-card-detail" , "business-cards/raised-spot-uv-business-card-detail",
                "business-cards/pantone-business-cards-detail", "business-cards/plastic-business-cards-detail",
                "business-cards/raised-ink-business-cards-detail"]
    ### Business Cards zip objects ###
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    ### Urls list for navbar BS products ###
    urls_bs_aside = ["business-stationary/envelopes-detail" , "business-stationary/letterhead-detail" , 
                     "business-stationary/notepad-detail"]
    ### Business Staionary zip objects ###
    bs_list_aside = zip(urls_bs_aside,bs_object_aside)
    ### Urls list for navbar lf products ###
    urls_lf_aside = ["large-format/floor-stickers-detail", "large-format/foamcore-poster-detail",
                "large-format/poster-printing-detail", "large-format/retractable-banners-detail",
                "large-format/table-cover-detail"]
    ### LF prodcuts zip objects ###
    lf_list_aside = zip(urls_lf_aside,lf_object_aside)
    ### Urls list for navbar mp products ###
    urls_mp_aside = ["marketing-products/postcards-detail","marketing-products/calenders-detail",
                "marketing-products/brouchers-flyers-detail", "marketing-products/hangtags-detail",
                "marketing-products/labels-and-stickers-detail", "marketing-products/ncr-forms-detail",
                "marketing-products/presentation-folder-detail","marketing-products/custom-holiday-cards-detail"]
    ### LF prodcuts zip objects ###
    mp_list_aside = zip(urls_mp_aside,mp_object_aside)
    ### Urls list Boxes prodcuts ###
    urls_b = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]

    ### Urls list navbar Boxes prodcuts ###
    urls_b_aside = ["boxes/pillow-boxes-detail", "boxes/gable-boxes-detail", 
            "boxes/window-boxes-detail", "boxes/mailer-boxes-detail", 
            "boxes/kraft-boxes-detail", "boxes/cosmetics-boxes-detail", 
            "boxes/sleeve-boxes-detail", "boxes/display-boxes-detail", 
            "boxes/beverage-boxes-detail", "boxes/candle-boxes-detail", 
            "boxes/auto-parts-boxes-detail", "boxes/pizza-boxes-detail" 
            ]
    ### Boxes Zip objects ###
    b_list = zip(urls_b,b_object)
    b_list_aside = zip(urls_b_aside, b_object_aside)

    context = {
        "b_list" : b_list,
        "bc_list_aside" : bc_aside,
        "bs_list_aside" : bs_list_aside,
        "lf_list_aside" : lf_list_aside,
        "mp_list_aside" : mp_list_aside,
        "b_list_aside"  : b_list_aside,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
        "b_card"  : b_card,
    }
    return render(request, "core/catogery.html", context)
# ------  Catogirze Pages in frontend  ------ # 
# ------  All pages are dynamic using if else and db ------ #
