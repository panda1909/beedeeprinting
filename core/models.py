from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class business_cards_price(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    digital_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    digital_Fast_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    offset_HQ = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    offset_HQ_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    description = models.CharField(default='Des',max_length=5000)

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

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "6 - Plastic business cards price"

class raised_ink_business_cards_price(models.Model):
    US_Standard_Size = models.CharField(max_length=555)
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "7 - Raised ink business cards price"


class Calendars(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    
    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "8 - Calendar"

class BrochuresAndFlyers(models.Model):
    quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = "9 - Brochures and Flyer"

class PostCards(models.Model):
   quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return str(self.quantity)

   class Meta:
        verbose_name = "10 - Post Card"

class QuotationPostCards(models.Model):
   PostCards = models.ForeignKey(PostCards, on_delete=models.CASCADE, related_name='PostCards')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return str(str(self.PostCards) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "10.1 - Quotation Post Card"


class DirectMailPostCards(models.Model):
   quantity = models.IntegerField(default=2, null=False)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "11 - Direct Mail PostCard"


class QuotationDirectMailPostCards(models.Model):
   DirectMailPostCards = models.ForeignKey(PostCards, on_delete=models.CASCADE, related_name='DirectMailPostCards')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.DirectMailPostCards) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "11.1 - Direct Mail PostCard"

class HangTags(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Three_By_Five_By_One_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.5" x 1.5"')
    Three_By_Five_By_One_By_Five_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.5" x 1.5" Discounted')
    Two_By_Five_By_Two_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2.5" x 2.5"')
    Two_By_Five_By_Two_By_Five_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2.5" x 2.5" Discounted')
    Two_By_Six = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 6"')
    Two_By_Six_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 6" Discounted')

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "12 - Hang Tag"

class LabelsAndStickers(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Two_By_Two = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 2"')
    Two_By_Two_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '2" x 2" Discounted')
    Three_By_Three = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3" x 3"')
    Three_By_Three_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3" x 3" Discounted')
    Four_By_Four = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '4" x 4"')
    Four_by_Four_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '4" x 4" Discounted')

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "13 - Labels And Sticker"

class NCRForms(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Five_By_Five_By_Eight_By_Five = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '5.5" x 8.5"')
    Five_By_Five_By_Eight_By_Five_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '5.5" x 8.5" Discounted')
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11"')
    Eight_By_Five_By_Eleven_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11" Discounted')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "14 - NCR Form"

class PresentationFolders(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Nine_By_Twelve_Fast = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Fast - Digital Fast')
    Nine_By_Twelve_Fast_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Digital Fast Discounted')
    Nine_By_Twelve_Offset = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Offset Folders')
    Nine_By_Twelve_Offset_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9" x 12" Offset Discounted')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "15 - Presentation Folder"

class CustomHolidayCards(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Folding_Card = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'Folding card - closed size is 5" x 7"')
    Folding_Card_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'Folding card - closed size is 5" x 7" Discounted')

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "16 - Custom Holiday Card"    

class Envelopes(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Number_10 = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '#10 (9.5x4.125)')
    Number_10_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '#10 (9.5x4.125) Discounted')
    Nine_By_Twleve = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9 x 12')
    Nine_By_Twleve_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9 x 12 Discounted')
    A7 = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'A7 (5.25X7.25)')
    A7_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'A7 (5.25X7.25) Discounted')


    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "17 - Envelope"

class LetterHeads(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11"')
    Eight_By_Five_By_Eleven_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11" Discounted')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "18 - LetterHead" 

class NotePads(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Three_By_Six_By_Four_By_Eight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.625" x 4.875"')
    Three_By_Six_By_Four_By_Eight_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.625" x 4.875" Discounted')
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "19 - NotePad"                           

class FoamcorePosters(models.Model):
   quantity = models.IntegerField(default=2, null=False)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "20 - Foamcore Poster"


class QuotationFoamcorePosters(models.Model):
   FoamcorePosters = models.ForeignKey(FoamcorePosters, on_delete=models.CASCADE, verbose_name='Foamcore Posters')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.FoamcorePosters) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "20.1 - Foamcore Poster"

class PosterPrinting(models.Model):
   quantity = models.IntegerField(default=2, null=False)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "21 - Poster Printing"

class QuotationPosterPrinting(models.Model):
   PosterPrinting = models.ForeignKey(PosterPrinting, on_delete=models.CASCADE, verbose_name='Poster Printing')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.PosterPrinting) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "21.1 - Poster Printing"

class RetractableBanners(models.Model):
    Quantity_From = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Quantity_To = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Thirty_Three_By_Eighty = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '33" x 80"')
    Thirty_Three_By_Eighty_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '33" x 80" Discounted')
    
    def __str__(self):
        return (str(self.Quantity_From)+ "-" + str(self.Quantity_To))

    class Meta:
        verbose_name = "22 - Retractable Banner"

class TableCovers(models.Model):
    Quantity_From = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Quantity_To = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Ninety_By_One_Three_Two = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '6 foot table cover (90" x 132")')
    Ninety_By_One_Three_Two_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '6 foot table cover (90" x 132") Discounted')
    
    def __str__(self):
        return (str(self.Quantity_From)+ "-" + str(self.Quantity_To))

    class Meta:
        verbose_name = "23 - Table Cover"     

class Orders(models.Model):
    OrderId = models.CharField(null=False, max_length=256)
    Customer = models.CharField(null=False, max_length=512)
    Status = models.CharField(null=False, max_length=256)
    Quantity = models.PositiveIntegerField(default=1, blank=False, editable=True)
    Size = models.CharField(null=False, max_length=1024)
    Price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])

    def __str__(self):
        return str(self.OrderId)

    class Meta:
        verbose_name = "24 - Orders Table"
        verbose_name_plural = "24 - Orders Table"

class CustomerData(models.Model):
    Name = models.CharField(null=False, max_length=1024)
    Email = models.CharField(null=False, max_length=1024)
    Cell = models.CharField(null=False, max_length=20)
    Address = models.CharField(null=False, max_length=2048)
    Orders = models.ManyToManyField(Orders)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = "25 - Customer Information"
        verbose_name_plural = "25 - Customer Information"

class FloorStickers(models.Model):
   quantity = models.IntegerField(default=2, null=False)

   def __str__(self):
       return str(self.quantity)

   class Meta:
       verbose_name = "26 - Floor Sticker"

class QuotationFloorStickers(models.Model):
   FloorStickers = models.ForeignKey(FloorStickers, on_delete=models.CASCADE, verbose_name='Floor Stickers')
   price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   price_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
   dimensionX = models.PositiveIntegerField(default=0, blank=False, editable=True)
   dimensionY = models.PositiveIntegerField(default=0, blank=False, editable=True)

   def __str__(self):
       return (str(self.FloorStickers) + " " + str(self.dimensionX) + "x" + str(self.dimensionY))

   class Meta:
       verbose_name = "26.1 - Floor Sticker"        