from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    def get(self, request):
        return render(request, 'core/contactus.html')


class Aboutus(TemplateView):
    def get(self, request):
        return render(request, 'core/aboutus.html')


class Cart(TemplateView):
    def get(self, request):
        return render(request, 'core/cart.html')
