from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(PostCards)
admin.site.register(QuotationPostCards)
admin.site.register(BrochuresAndFlyers)
admin.site.register(DirectMailPostCards)
admin.site.register(QuotationDirectMailPostCards)
admin.site.register(Calendars)
admin.site.register(HangTags)
admin.site.register(LabelsAndStickers)
admin.site.register(NCRForms)
admin.site.register(PresentationFolders)
admin.site.register(CustomHolidayCards)
# admin.site.register(Templates)


# class TemplatesAdmin(admin.StackedInline):
#     model = Templates