from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class FoamcorePosters(models.Model):
   Quantity = models.IntegerField(default=0, blank=True ,verbose_name='Quantity')
   Discount = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
   Twelve_By_Eighteen = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='12" x 18" Cost')
   Eighteen_By_TwentyFour = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='18" x 24" Cost')
   TwentyFour_By_TwentyFour = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='24" x 24" Cost')
   Twenty_By_Thrity = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='20" x 30" Cost')
   TwentyFour_By_ThirtySix = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='24" x 36" Cost')
   ThirtySix_By_FourtyEight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='36" x 48" Cost')
   FourtySix_By_FourtyEight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='46" x 48" Cost')

   
   def __str__(self):
       return (str(self.Quantity) + " " + str(self.Discount))

   class Meta:
       verbose_name = "1 - Foamcore Poster"

class PosterPrinting(models.Model):
    Quantity = models.IntegerField(default=0, blank=True ,verbose_name='Quantity')
    Discount = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    Eighteen_By_TwentyFour = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='18" x 24" Cost')
    Twenty_By_Thrity = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='20" x 30" Cost')
    TwentyFour_By_ThirtySix = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='24" x 36" Cost')
    TwentySeven_By_Forty = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='27" x 40" Cost')
    ThirtySix_By_FourtyEight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='36" x 48" Cost')
    FourtyEight_By_FourtyEight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='48" x 48" Cost')
    SeventyTwo_By_TwentyFour = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='72" x 24" Cost')

    def __str__(self):
       return str(self.Quantity)

    class Meta:
       verbose_name = "2 - Poster Printing"


class RetractableBanners(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Thirty_Three_By_Eighty = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '33" x 80"')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '33" x 80" Discounted')
    # Template = models.FileField(upload_to='static/Large_Format_Printing_Templates', max_length=256, blank=True)
    Template1 = models.FileField(upload_to='', default='')

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "3 - Retractable Banner"

class TableCovers(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Ninety_By_One_Three_Two = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '6 foot table cover (90" x 132")')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "4 - Table Cover"     

class FloorStickers(models.Model):
   Quantity = models.IntegerField(default=2, null=False)
   Twelve_By_Twelve = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='12" x 12" Square Cost')
   TwentyFour_By_TwentyFour = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='24" x 24" Square Cost')
   Eighteen_By_TwentyFour = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='18" x 24" Rectangle Cost')
   ThirtySix_By_FourtyEight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='36" x 48" Rectangle Cost')
   Eighteen = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name='18" Circle Cost')
   Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
   Template1 = models.FileField(upload_to='', default='')

   def __str__(self):
       return str(self.Quantity)

   class Meta:
       verbose_name = "5 - Floor Sticker"
      

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Large_Format_Printing/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Large_Format_Printing/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Large_Format_Printing/',max_length=None)

    def __str__(self):
        return(self.Label)
    
    class Meta:
        verbose_name = "Product List"   

class Extra_features(models.Model):
    banner_material = models.CharField(max_length=250, blank=True)
    banner_material_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])    
    second_side_printing_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return(self.banner_material)

    class Meta:
        verbose_name = "0 - Extra Feature"
        