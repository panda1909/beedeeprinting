from django import forms
from .models import Orders
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .validators import validate_file_extension
from Business_Cards.models import business_cards_price, Extra_features
from core.models import Messages




class ImageFileUploadForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Template',)


class checkoutForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Country = forms.CharField(max_length=100)
    Zipcode = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    Region = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=500)
    Email = forms.EmailField()
    Mobile = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'e.g. +12125552368'}))
    Phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'e.g. +12125552368'}))
    TemplateOne = forms.FileField(required=False ,validators=[validate_file_extension])
    TemplateTwo = forms.FileField(required=False ,validators=[validate_file_extension])
    Notes_Requests =  forms.CharField(widget=forms.Textarea, required=False)



class queries(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['Subject','Message','Name','Email']