from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
import json
# All category products
from Business_Cards.models import Products as bc_products 
from Business_Cards.models import business_cards_price, Extra_features
from Business_Stationary.models import Products as bs_products
from Large_Format_Printing.models import Products as lf_products
from Marketing_Products.models import Products as mp_products

# order and customer table
from .models import Orders, CustomerData

from django.http import HttpResponse
from django.template import loader
from .form import checkoutForm
import shortuuid



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
        discount_query = business_cards_price.objects.raw('SELECT id, Discount FROM Business_Cards_business_cards_price WHERE quantity = %s', [quantity])
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
            price_paper = i.paper_type_price

        for o in size_query:
            price_size = o.size_price
        
        for p in type_quantity_query:
            if printing_type == 'digital_Fast':
                price_type = p.digital_Fast
            elif printing_type == 'offset_HQ':
                price_type = p.offset_HQ
        
        for y in discount_query:
            price_discount = y.Discount
                
                
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
    }
    if request.POST:
        return redirect('checkout')
    return render(request, "core/detail.html", context)



class Aboutus(TemplateView):
    def get(self, request):
        return render(request, 'core/aboutus.html')

def Checkout(request):
    try:
        total = request.session['invoice']
        label = request.session['label']
        discount = request.session['discount']
        id = request.session['id']
        category = request.session['cat']
        quantity = request.session['quantity']
        extra_f_dict = request.session['extra_f']
        print('CHeckout try')
        json_dump = json.dumps(extra_f_dict)
        json_obj = json.loads(json_dump)
        size = extra_f_dict['size']
    except:
        return HttpResponse("Your cart is empty")

    if category == 'bc_products':
        product = bc_products.objects.get(id=id)
        print(category, id)
    elif category == 'bs_prodcuts':
        product = bs_products.objects.get(id=id)
        print(category, id)
    elif category == 'lf_products':
        product = lf_products.objects.get(id=id)
        print(category, id)
    elif category == 'mp_products':
        product = mp_products.objects.get(id=id)
        print(category, id)

    print(product)

    price = total - discount
    tax = price * .16
    round_tax = round(tax,2)
    tax = round_tax
    price_final = price + tax
    order_id = shortuuid.ShortUUID().random(length=12)
    # shipping info form
    if request.method == 'POST':
       print("--------> POST")
       form = checkoutForm(request.POST)
    #    print (form)
       if form.is_valid():
            Name = form.cleaned_data["FirstName"]+" "+form.cleaned_data["LastName"]
            Country = form.cleaned_data["Country"]
            City = form.cleaned_data["City"]
            Region = form.cleaned_data["Region"]
            Address = form.cleaned_data["Address"]
            Email = form.cleaned_data["Email"]
            Mobile = form.cleaned_data["Mobile"]
            Phone = form.cleaned_data["Phone"]
            Notes_Requests = form.cleaned_data["Notes_Requests"]
            TemplateOne = form.cleaned_data["TemplateOne"]
            TemplateTwo = form.cleaned_data["TemplateTwo"]
            Notes_Requests =  form.cleaned_data["Notes_Requests"]
            zipcode = form.cleaned_data["Zipcode"]

            # session for order id page
            request.session['Name'] = Name
            request.session['order_id'] = order_id

            # print(Name)
            order = Orders.objects.create(Customer=Name, Country=Country, City=City, Region=Region, Email=Email, Delivery_address=Address,  Mobile=Mobile, Contact = Phone, Special_requests=Notes_Requests, Zip_Code=zipcode, Extra_features=json_obj, Price=price_final, Quantity=quantity , Size=size, Product_name=label, OrderId=order_id, Status="Pending")

          
            if CustomerData.objects.filter(Email=Email).exists() :
                Customerinfo = CustomerData.objects.get(Email=Email)
                print(Customerinfo)
                Customerinfo.Orders.add(order)
            else:
                Customerinfo = CustomerData.objects.create(Name=Name, Email=Email, Cell=Mobile, Country=Country, Region=Region, City=City, Zip_Code=zipcode, Address=Address)
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
    }
    return render(request, 'core/checkout.html', context)

def Order_placed(request):
    Name = request.session['Name']
    order_id = request.session['order_id'] 
    context = {
        'Name' : Name,
        'order_id' : order_id,
    }
    del request.session['invoice']
    return render(request, 'core/order_placed.html', context)


def get_status(request):
    status = "Please Enter ID first."
    check = 0
    if request.POST:
        form = request.POST
        Order_id = form['Order_id']
        print("---------->>>>", Order_id)
        status_query = Orders.objects.raw("SELECT id, Status FROM core_Orders WHERE OrderId = %s",[Order_id])
        for p in status_query:
            status = p.Status
    context={
        'status' : status,
        'check' : check,
    }
    return render(request, 'core/get_status.html', context)


def Cart(request):
    return render(request, 'core/cart.html')

# ------  All Products page/funct  ------ # 

def All_products(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc = ["detail","business-cards"]
    bc_list = zip(urls_bc,bc_object)

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_list"    : bc_list,
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