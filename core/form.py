from django import forms
from .models import Orders
from django.forms import ModelForm
<<<<<<< HEAD
=======
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file_extension
from Business_Cards.models import business_cards_price, Extra_features
>>>>>>> 63b0b5b8c31f513f6a69dbde81034f9189a63f6c



class ImageFileUploadForm (forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('Template',)
<<<<<<< HEAD
=======


class checkoutForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Country = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    Region = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=500)
    Email = forms.EmailField()
    Mobile = PhoneNumberField()
    Phone = PhoneNumberField()
    TemplateOne = forms.ImageField(upload_to = 'static/Order_Templates/', blank=True ,validators=[validate_file_extension])
    TemplateTwo = forms.ImageField(upload_to = 'static/Order_Templates/', blank=True ,validators=[validate_file_extension])
>>>>>>> 63b0b5b8c31f513f6a69dbde81034f9189a63f6c
