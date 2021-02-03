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
from boxes.models import Products as b_products

# order and customer table
from .models import Orders, CustomerData
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader
from .form import checkoutForm,queries, bookcalls
import shortuuid



# Create your views here.

def Home(request):
    form = bookcalls(request.POST)
    context = {
        "form": form
    }
    return render(request, "core/index.html", context)
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
    print('Checkout try')
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
       form = checkoutForm(request.POST)
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
            TemplateOne = form.cleaned_data["TemplateOne"]
            TemplateTwo = form.cleaned_data["TemplateTwo"]
            Notes_Requests =  form.cleaned_data["Notes_Requests"]
            zipcode = form.cleaned_data["Zipcode"]

            # session for order id page
            request.session['Name'] = Name
            request.session['order_id'] = order_id
            request.session['email'] = Email

            # print(Name)
            order = Orders.objects.create(Customer=Name, Country=Country, City=City, Region=Region, Email=Email, Delivery_address=Address, Contact = Phone, Special_requests=Notes_Requests, Zip_Code=zipcode, Extra_features=json_obj, Price=price_final, Quantity=quantity , Size=size, Product_name=label, OrderId=order_id, Status="Pending")

          
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
    Name = request.session['Name']
    email = request.session['email']
    order_id = request.session['order_id'] 
    subject = "Order ID"
    final_message= "Your Order Id:"+" "+order_id 
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
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    urls_bc = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail"]
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail"]
    bc_list = zip(urls_bc,bc_object)
    bc_aside = zip(urls_bc_aside,bc_object_aside)
    print("------->> list",bc_list)
    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_list"    : bc_list,
        "bc_aside"   : bc_aside,
    }
    return render(request, "core/all_products.html", context)

# ------  Catogirze Pages in frontend  ------ #
# ------  All pages are dynamic using if else and db ------ #

def Business_card(request):
    bc_object = bc_products.objects.all()
    bs_object = bs_products.objects.all()
    lf_object = lf_products.objects.all()
    mp_object = mp_products.objects.all()
    bc_object_aside = bc_products.objects.all()
    bc_card = 1
    bs_card = 0
    lf_card = 0
    mp_card = 0

    urls_bc = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail"]
    urls_bc_aside = ["business-cards/business-card-detail" , "business-cards/edge-painted-detail"]
    bc_list = zip(urls_bc,bc_object)
    bc_aside = zip(urls_bc_aside,bc_object_aside)

    context = {
        "bc_product" : bc_object,
        "bs_product" : bs_object,
        "lf_product" : lf_object,
        "mp_product" : mp_object,
        "bc_card" : bc_card,
        "bs_card" : bs_card,
        "lf_card" : lf_card,
        "mp_card" : mp_card,
        "bc_list"    : bc_list,
        "bc_aside"   : bc_aside,
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
