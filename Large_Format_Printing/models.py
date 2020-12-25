from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class FoamcorePosters(models.Model):
   quantity = models.IntegerField(default=2, null=False)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "1 - Foamcore Poster"


class QuotationFoamcorePosters(models.Model):
   FoamcorePosters = models.ForeignKey(FoamcorePosters, on_delete=models.CASCADE, verbose_name='Foamcore Posters')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.FoamcorePosters) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "1.1 - Foamcore Poster"

class PosterPrinting(models.Model):
   quantity = models.IntegerField(default=2, null=False)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "2 - Poster Printing"

class QuotationPosterPrinting(models.Model):
   PosterPrinting = models.ForeignKey(PosterPrinting, on_delete=models.CASCADE, verbose_name='Poster Printing')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.PosterPrinting) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "2.1 - Poster Printing"

class RetractableBanners(models.Model):
    Quantity_From = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Quantity_To = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Thirty_Three_By_Eighty = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '33" x 80"')
    Thirty_Three_By_Eighty_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '33" x 80" Discounted')
    Template = models.ImageField(upload_to='static/Large_Format_Printing_Templates', max_length=256, blank=True)

    def __str__(self):
        return (str(self.Quantity_From)+ "-" + str(self.Quantity_To))

    class Meta:
        verbose_name = "3 - Retractable Banner"

class TableCovers(models.Model):
    Quantity_From = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Quantity_To = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Ninety_By_One_Three_Two = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '6 foot table cover (90" x 132")')
    Ninety_By_One_Three_Two_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '6 foot table cover (90" x 132") Discounted')

    def __str__(self):
        return (str(self.Quantity_From)+ "-" + str(self.Quantity_To))

    class Meta:
        verbose_name = "4 - Table Cover"     

class FloorStickers(models.Model):
   quantity = models.IntegerField(default=2, null=False)
   
   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "5 - Floor Sticker"

class QuotationFloorStickers(models.Model):
   FloorStickers = models.ForeignKey(FloorStickers, on_delete=models.CASCADE, verbose_name='Floor Stickers')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.FloorStickers) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "5.1 - Floor Sticker"        

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Large_Format_Printing/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Large_Format_Printing/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Large_Format_Printing/',max_length=None)

    def __str__(self):
        return(self.Label)
    
    class Meta:
        verbose_name = "0 - Product List"       