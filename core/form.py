from django import forms
from .models import Orders
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from .validators import validate_file_extension
from Business_Cards.models import business_cards_price, Extra_features
from core.models import Messages, Bookedcalls




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
    # Mobile = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'e.g. +12125552368'}))
    Phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'e.g. +12125552368'}))
    TemplateOne = forms.FileField(required=False ,validators=[validate_file_extension])
    TemplateTwo = forms.FileField(required=False ,validators=[validate_file_extension])
    Notes_Requests =  forms.CharField(widget=forms.Textarea, required=False)



class queries(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['Subject','Message','Name','Email','Contacted']
        
class bookcalls(forms.ModelForm):
    class Meta:
        model = Bookedcalls
        fields = ['Name', 'Email', 'Cell', 'Time', 'Date', 'Description']

      


# CHOICES: #
Unit_CHOICES = (
        ('cm', 'cm'),
        ('mm', 'mm'),
        ('inches', 'inches'),
)       

Color_CHOICES = (
    ('1-color', '1-color'),
    ('2-color', '2-color'),
    ('3-color', '3-color'),
    ('4-color', '4-color'),
    ('4/1-color', '4/1-color'),
    ('4/2-color', '4/2-color'),
    ('4/3-color', '4/3-color'),
    ('4/4-color', '4/4-color'),
)

Stock_CHOICES = (
    ('12pt', '12pt'),
    ('14pt', '14pt'),
    ('16pt', '16pt'),
    ('18pt', '18pt'),
    ('20pt', '20pt'),
    ('22pt', '22pt'),
    ('24pt', '24'),
    ('Card Stock', 'Card Stock'),
    ('Kraft Stock', 'Kraft Stock'),
    ('Corrugated Stock', 'Corrugated Stock'),

)

class BoxcheckoutForm(forms.Form):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Country = forms.CharField(max_length=100)
    Zipcode = forms.CharField(max_length=100)
    City = forms.CharField(max_length=100)
    Region = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=500)
    Email = forms.EmailField()
    Phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'e.g. +12125552368'}))
    Width = forms.IntegerField(required=False)
    Height = forms.IntegerField(required=False)
    Depth = forms.IntegerField(required=False)
    Unit = forms.ChoiceField(choices=Unit_CHOICES)
    Quantity = forms.IntegerField(required=True)
    Color = forms.ChoiceField(choices=Color_CHOICES)
    Stock = forms.ChoiceField(choices=Stock_CHOICES)
    Notes_Requests =  forms.CharField(widget=forms.Textarea, required=False)
