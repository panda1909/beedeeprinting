from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(PostCards)
admin.site.register(BrochuresAndFlyers)
admin.site.register(Calendars)
admin.site.register(HangTags)
admin.site.register(LabelsAndStickers)
admin.site.register(NCRForms)
admin.site.register(PresentationFolders)
admin.site.register(CustomHolidayCards)
admin.site.register(Extra_features)
admin.site.register(Products)


# class TemplatesAdmin(admin.StackedInline):
#     model = Templates