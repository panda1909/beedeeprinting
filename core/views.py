from django.shortcuts import render
from django.views.generic import TemplateView
from Marketing_Products.models import Calendars
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def detail_calender(request):
    query_set = Calendars.objects.get(id=2)
    # template = loader.get_template('core/detail.html')
    context = {
        "Des": query_set.Description,
        "label": query_set.label,
        "image" : query_set.image,
    }
    # print(Des.Description)
    return render(request, "core/detail.html", context)

def Home(request):
    return render(request, "core/all_products.html")

class Aboutus(TemplateView):
    def get(self, request):
        return render(request, 'core/aboutus.html')


class Cart(TemplateView):
    def get(self, request):
        return render(request, 'core/cart.html')
