from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    digital_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    digital_Fast_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    offset_HQ = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    offset_HQ_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)
    

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "1 - Simple business cards price"    

class edge_painted_business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    US_Standard_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    US_Standard_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    European_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    European_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Square = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Square_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "2 - Edge painted business cards price"    

class foil_business_cards_price(models.Model):
    US_Standard_size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "3 - Foil business cards price"

class raised_spot_uv_business_cards_price(models.Model):
    US_Standard_size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "4 - Raised spot UV business cards price"

class pantone_business_cards_price(models.Model):
    US_Standard_Size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "5 - Pantone business cards price"

class plastic_business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    US_Standard_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="US Standard Size Price")
    US_Standard_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="US Standard Size Price Discounted")
    Credit_card_Size = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="Credit Card Size Price")
    Credit_card_Size_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name="Credit Card Size Price Discounted")
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "6 - Plastic business cards price"

class raised_ink_business_cards_price(models.Model):
    US_Standard_Size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "7 - Raised ink business cards price"

