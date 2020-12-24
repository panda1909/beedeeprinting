from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Calendars(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "1 - Calendar"

class BrochuresAndFlyers(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "2 - Brochures and Flyer"

class PostCards(models.Model):
   quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
   Description = models.TextField(default='des',max_length=2048)
   
   def __str__(self):
       return str(self.quantity)

   class Meta:
        verbose_name = "3 - Post Card"


# CARD_CHOICES=[
#     ('PostCards/','PostCards')
#     ,('QuotationPostCards/','QuotationPostCards')
#     ,('BrochuresAndFlyers/','BrochuresAndFlyers')
#     ,('DirectMailPostCards/','DirectMailPostCards')
#     ,('QuotationDirectMailPostCards/','QuotationDirectMailPostCards')
#     ,('Calendars/','Calendars')
#     ,('HangTags/','HangTags')
#     ,('LabelsAndStickers/','LabelsAndStickers')
#     ,('NCRForms/','NCRForms')
#     ,('PresentationFolders/','PresentationFolders')
#     ,('CustomHolidayCards/','CustomHolidayCards')
#     ]



# class Templates(models.Model):
#     card = models.CharField(max_length=256,choices=CARD_CHOICES)
#     file = models.FileField(upload_to='static/' +str(card), max_length=256)


class QuotationPostCards(models.Model):
   PostCards = models.ForeignKey(PostCards, on_delete=models.CASCADE, related_name='PostCards')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)
   
#    templates = models.ManyToManyField(Templates)

   def __str__(self):
       return str(str(self.PostCards) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "3.1 - Quotation Post Card"


class DirectMailPostCards(models.Model):
   quantity = models.IntegerField(default=2, null=False)
   Description = models.TextField(default='des',max_length=2048)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "4 - Direct Mail PostCard"


class QuotationDirectMailPostCards(models.Model):
   DirectMailPostCards = models.ForeignKey(PostCards, on_delete=models.CASCADE, related_name='DirectMailPostCards')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.DirectMailPostCards) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "4.1 - Direct Mail PostCard"

class HangTags(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Three_By_Five_By_One_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.5" x 1.5"')
    Three_By_Five_By_One_By_Five_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.5" x 1.5" Discounted')
    Two_By_Five_By_Two_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2.5" x 2.5"')
    Two_By_Five_By_Two_By_Five_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2.5" x 2.5" Discounted')
    Two_By_Six = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 6"')
    Two_By_Six_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 6" Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "5 - Hang Tag"

class LabelsAndStickers(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Two_By_Two = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 2"')
    Two_By_Two_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 2" Discounted')
    Three_By_Three = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3" x 3"')
    Three_By_Three_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3" x 3" Discounted')
    Four_By_Four = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '4" x 4"')
    Four_by_Four_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '4" x 4" Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "6 - Labels And Sticker"

class NCRForms(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Five_By_Five_By_Eight_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '5.5" x 8.5"')
    Five_By_Five_By_Eight_By_Five_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '5.5" x 8.5" Discounted')
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11"')
    Eight_By_Five_By_Eleven_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11" Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "7 - NCR Form"

class PresentationFolders(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Nine_By_Twelve_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Fast - Digital Fast')
    Nine_By_Twelve_Fast_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Digital Fast Discounted')
    Nine_By_Twelve_Offset = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Offset Folders')
    Nine_By_Twelve_Offset_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Offset Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "8 - Presentation Folder"

class CustomHolidayCards(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Folding_Card = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'Folding card - closed size is 5" x 7"')
    Folding_Card_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'Folding card - closed size is 5" x 7" Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "9 - Custom Holiday Card"    

