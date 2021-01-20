from django import forms
from .models import Orders
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .validators import validate_file_extension
from Business_Cards.models import business_cards_price, Extra_features



class ImageFileUploadForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Template',)


class checkoutForm(forms.Form):
    FirstName = forms.CharField(max_length=100 )
    LastName = forms.CharField(max_length=100)
    Country = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    Region = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=500)
    Email = forms.EmailField()
    Mobile = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    Phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    TemplateOne = forms.FileField(required=False ,validators=[validate_file_extension])
    TemplateTwo = forms.FileField(required=False ,validators=[validate_file_extension])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Mobile'].widget.attrs.update({'placeholder': 'e.g. +12125552368'})
        self.fields['Phone'].widget.attrs.update({'placeholder': 'e.g. +12125552368'})

