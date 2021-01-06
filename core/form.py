from django import forms
from .models import Orders
from django.forms import ModelForm
from Business_Cards.models import business_cards_price, Extra_features


class ImageFileUploadForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Template',)


class BusinessCard(forms.Form):
    offset_HQ = business_cards_price._meta.get_field('offset_HQ')
    digital_Fast = business_cards_price._meta.get_field('digital_Fast')
    choice = (
        (digital_Fast.name, digital_Fast.name),
        (offset_HQ.name,offset_HQ.name),
    )
    queryset = business_cards_price.objects.values_list('offset_HQ', flat=True)
    TurnaroundTime = forms.ChoiceField(choices=choice)
    Quantity = forms.ModelChoiceField(queryset=business_cards_price.objects.all())
