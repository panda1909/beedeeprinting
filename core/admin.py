from django.contrib import admin    
from .models import *

# Register your models here.
# class OrdersAdmin(admin.ModelAdmin):
#     list_display = ['OrderId','Customer','Status','Quantity','Size','Price']
#     #list_editable = ['OrderId','Customer','Status','Quantity','Size','Price']
# class CustomerDataAdmin(admin.ModelAdmin):
#     list_display = ['Name','Email','Address']

admin.site.register(Orders)
admin.site.register(CustomerData)
admin.site.register(Messages)
admin.site.register(Bookedcalls)
