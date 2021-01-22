from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Calendars(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "1 - Calendar"

class BrochuresAndFlyers(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "2 - Brochures and Flyer"

class PostCards(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Discount = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    Template = models.FileField(upload_to='static/Marketing_Products_Templates', max_length=256, blank=True)
    Two_By_Eight = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='2" x 8" Cost')
    Three_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='3" x 5" Cost')
    Three_By_Five_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='3.5" x 5" Cost')
    Four_By_Twelve = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4" x 12" Cost')
    Four_By_Four = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4" x 4" Cost')
    Four_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4" x 5" Cost')
    Four_By_Six = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4" x 6" Cost')
    Four_By_Nine = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4" x 9" Cost')
    Four_By_TwoFive_By_Eleven = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4.25" x 11" Cost')
    Four_By_TwoFive_By_FiveByFive = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4.25" x 5.5" Cost')
    Five_By_Seven = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='5" x 7" Cost')
    Four_By_TwoFive_By_Six = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4.25" x 6" Cost')
    Four_By_TwoFive_By_Nine = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4.25" x 9" Cost')
    Four_By_Five_By_Twelve = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='4.5" x 12" Cost')
    Five_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='5" x 5" Cost')
    Eight_By_Five_By_Five_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='8.5" x 5.5" Cost')
    Six_By_Eleven = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='6" x 11" Cost')
    Six_By_Six = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='6" x 6" Cost')
    Six_By_Nine = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='6" x 9" Cost')
    Six_By_TwoFive_By_Eleven = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='6.25" x 11" Cost')
    Six_By_TwoFive_By_Nine = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='6.25" x 9" Cost')    
    Six_By_Five_By_Eleven = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='6.5" x 9" Cost')
    Eight_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='8" x 5" Cost')
    Eight_By_Five_By_Three_By_Five = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='8.5" x 3.5" Cost')
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)], verbose_name='8.5" x 11" Cost')


    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "3 - Post Card"


class HangTags(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Three_By_Five_By_One_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '3.5" x 1.5"')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    Two_By_Five_By_Two_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '2.5" x 2.5"')
    Two_By_Six = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '2" x 6"')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "5 - Hang Tag"

class LabelsAndStickers(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Two_By_Two = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '2" x 2"')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    Three_By_Three = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '3" x 3"')
    Four_By_Four = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '4" x 4"')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "6 - Labels And Sticker"

class NCRForms(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Five_By_Five_By_Eight_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '5.5" x 8.5"')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '8.5" x 11"')

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "7 - NCR Form"

class PresentationFolders(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')
    Template = models.FileField(upload_to='static/Marketing_Products_Templates', max_length=256, blank=True)
    Nine_By_Twelve_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '9" x 12" Fast - Digital Fast')
    Nine_By_Twelve_Offset = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = '9" x 12" Offset Folders')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "8 - Presentation Folder"

class CustomHolidayCards(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Folding_Card = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Folding card - closed size is 5" x 7"')
    Discount = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.0)], verbose_name = 'Folding card - closed size is 5" x 7" Discounted')
    Template = models.FileField(upload_to='static/Marketing_Products_Templates', max_length=256, blank=True)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "9 - Custom Holiday Card"    

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Marketing_Products/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Marketing_Products/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Marketing_Products/',max_length=None)

    def __str__(self):
        return(self.Label)
    
    class Meta:
        verbose_name = "Product List"

class Extra_features(models.Model):
    second_side_printing_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    flat_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    half_fold_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    tri_fold_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    z_fold_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    double_parallel_fold_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    individual_cut_labels_price =  models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    three_part_form_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    form_numbering_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    paper_type = models.CharField(blank=True, max_length=250)
    paper_type_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])
    blank_envelope_price = models.FloatField(default=0, blank=True, editable=True, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return("extra Features")

    class Meta:
        verbose_name = "0 - Extra Feature"