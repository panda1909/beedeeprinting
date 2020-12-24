from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Envelopes(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Number_10 = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '#10 (9.5x4.125)')
    Number_10_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '#10 (9.5x4.125) Discounted')
    Nine_By_Twleve = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9 x 12')
    Nine_By_Twleve_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '9 x 12 Discounted')
    A7 = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'A7 (5.25X7.25)')
    A7_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = 'A7 (5.25X7.25) Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "1 - Envelope"

class LetterHeads(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Eight_By_Five_By_Eleven = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11"')
    Eight_By_Five_By_Eleven_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '8.5" x 11" Discounted')
    Description = models.TextField(default='des',max_length=2048)

    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "2 - LetterHead" 

class NotePads(models.Model):
    Quantity = models.PositiveIntegerField(default=0, blank=False, editable=True)
    Three_By_Six_By_Four_By_Eight = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.625" x 4.875"')
    Three_By_Six_By_Four_By_Eight_Discounted = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)], verbose_name = '3.625" x 4.875" Discounted')
    Description = models.TextField(default='des',max_length=2048)
    
    def __str__(self):
        return str(self.Quantity)

    class Meta:
        verbose_name = "3 - NotePad" 