from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Envelopes(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Number_10 = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '#10 (9.5x4.125)')
    Nine_By_Twleve = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '9 x 12')
    A7 = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'A7 (5.25X7.25)')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    # Template1 = models.FileField(upload_to='', default='')
    Template1 = models.FileField(upload_to='', default='')

    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "1 - Envelope"

class LetterHeads(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '8.5" x 11"')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    # Template = models.FileField(upload_to='static/Business_Stationary_Templates', max_length=256, blank=True)
    Template1 = models.FileField(upload_to='', default='')
    

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "2 - LetterHead" 

class NotePads(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Three_By_Six_By_Four_By_Eight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '3.625" x 4.875"')
    Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "3 - NotePad" 

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Business_Stationary/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Business_Stationary/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Business_Stationary/',max_length=None)

    def __str__(self):
        return(self.Label)
    
    class Meta:
        verbose_name = "Product List"        


class Extra_features(models.Model):
    paper_type = models.CharField(max_length=250, blank=True)
    paper_type_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    standard_window_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    second_side_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])


    def __str__(self):
        return (self.paper_type)

    class Meta:
        verbose_name = "0 - Extra Feature"