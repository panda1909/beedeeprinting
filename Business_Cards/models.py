from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    digital_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    digital_Fast_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Digital_Fast_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    offset_HQ = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    offset_HQ_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Offset_HQ_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "1 - Simple business cards price"    

class edge_painted_business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    US_Standard_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    US_Standard_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    US_Standard_Size_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    European_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    European_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    European_Size_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    Square = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Square_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Square_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "2 - Edge painted business cards price"    

class foil_business_cards_price(models.Model):
    US_Standard_size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "3 - Foil business cards price"

class raised_spot_uv_business_cards_price(models.Model):
    US_Standard_size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "4 - Raised spot UV business cards price"

class pantone_business_cards_price(models.Model):
    US_Standard_Size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "5 - Pantone business cards price"

class plastic_business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    US_Standard_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="US Standard Size Price")
    US_Standard_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="US Standard Size Price Discounted")
    US_Standard_Size_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    Credit_card_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="Credit Card Size Price")
    Credit_card_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="Credit Card Size Price Discounted")
    Credit_card_Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "6 - Plastic business cards price"

class raised_ink_business_cards_price(models.Model):
    US_Standard_Size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Template = models.ImageField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "7 - Raised ink business cards price"

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)

    def __str__(self):
        return(self.Label)
    
    class Meta:
        verbose_name = "0 - Product List"