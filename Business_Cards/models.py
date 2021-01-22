from django.db import models
from django.core.validators import MinValueValidator
#import django_tables2 as tables


# Create your models here.

class business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True,  )
    digital_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    offset_HQ = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Discount = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "1 - Simple business cards"  
  

class edge_painted_business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    US_Standard_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    US_Standard_Size_Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    European_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    European_Size_Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    Square = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Square_Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    Discount = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])    
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "2 - Edge painted business cards"    


class foil_business_cards_price(models.Model):
    US_Standard_size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "3 - Foil business cards"

class raised_spot_uv_business_cards_price(models.Model):
    US_Standard_size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "4 - Raised spot UV business cards"

class pantone_business_cards_price(models.Model):
    US_Standard_Size = models.CharField(max_length=555, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "5 - Pantone business cards"

class plastic_business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    US_Standard_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name="US Standard Size Price")
    Credit_card_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name="Credit Card Size Price")
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "6 - Plastic business cards"

class raised_ink_business_cards_price(models.Model):
    US_Standard_Size =  models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Business_Cards_Templates', max_length=256, blank=True)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "7 - Raised ink business cards"

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)

    def __str__(self):
        return(self.Label)
    
    class Meta:
        verbose_name = "Product List"

class Extra_features(models.Model):
    size = models.CharField(max_length=50, blank=True,  )
    size_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)],  )
    paper_type = models.CharField(max_length=250, blank=True,  )
    paper_type_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)],  )
    second_side_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)],  )
    second_side_foil_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    second_side_raied_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)],  )
    traditional_raised_printing_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    plastic_type = models.CharField(max_length=250, blank=True)
    plastic_type_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    raised_ink_colors = models.CharField(max_length=250, blank=True)
    rasied_ink_colors_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])


    def __str__(self):
        return str(self.size + self.paper_type)


    class Meta:
        verbose_name = "0 - Extra Feature"        
