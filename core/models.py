from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file_extension

                          
class Orders(models.Model):
    # Status Choices
    CHOICES = (
        ('Pending', 'Pending'),
        ('Printing', 'Printing'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
        ('Designing', 'Designing'),
    )
    OrderId = models.CharField(null=False, max_length=256)
    Product_name = models.CharField(null=False, max_length=512, default='pd')
    Customer = models.CharField(null=False, max_length=512)
    Country = models.CharField(null=False, max_length=512, default='Co')
    Region = models.CharField(null=False, max_length=512, default='R')
    City = models.CharField(null=False, max_length=512, default='Ci')
    Zip_Code = models.PositiveIntegerField(null=False)
    Delivery_address = models.CharField(null=False, max_length=1000, default='pd')
    Mobile = PhoneNumberField(blank=True)
    Contact = PhoneNumberField()
    Email = models.EmailField()
    Delivery_date = models.DateField(null=True, auto_now=False, auto_now_add=False)
    Status = models.CharField(null=False, max_length=256, choices=CHOICES, default='Pending')
    Quantity = models.PositiveIntegerField(default=1, blank=False, editable=True)
    Size = models.CharField(null=False, max_length=1024)
    Price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Template = models.FileField(upload_to='static/Order_templates', blank=True ,max_length=256, validators=[validate_file_extension])
    Second_Template = models.FileField(upload_to='static/Order_templates', blank=True, max_length=256, validators=[validate_file_extension])
    Special_requests = models.CharField(max_length=5000, blank=True)
    Extra_features = models.JSONField(default=dict)

    def __str__(self):
        return str((self.OrderId) + ' / ' + str(self.Product_name) + ' / ' + str(self.Customer))

    class Meta:
        verbose_name = "1 - Orders Table"
        verbose_name_plural = "1 - Orders Table"

class CustomerData(models.Model):
    Name = models.CharField(null=False, max_length=1024)
    Email = models.EmailField(max_length=254)
    Cell = PhoneNumberField()
    Country = models.CharField(null=False, max_length=512, default='Co')
    Region = models.CharField(null=False, max_length=512, default='R')
    City = models.CharField(null=False, max_length=512, default='Ci')
    Zip_Code = models.PositiveIntegerField(null=False)
    Address = models.CharField(null=False, max_length=2048)
    Orders = models.ManyToManyField(Orders)

    def __str__(self):
        return (str(self.Name) + " / " + str(self.Email))

    class Meta:
        verbose_name = "2 - Customer Information"
        verbose_name_plural = "2 - Customer Information"

class Messages(models.Model):
    Subject = models.CharField(max_length=1000)
    Message = models.TextField(max_length=5000)
    Name = models.CharField(null=False, max_length=1024)
    Email = models.EmailField()
    Contacted = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.Subject)

    class Meta:
        verbose_name = "3 - Clientle queries"
        verbose_name_plural = "3 - Clientle queries"

class Bookedcalls(models.Model):
    Name =models.CharField(max_length=100)
    Email =models.EmailField()
    Cell = PhoneNumberField()
    Time = models.TimeField()
    Date = models.DateField()
    Description = models.TextField(max_length=2000)

    def __str__(self):
        return (str(self.Name) + " / " + str(self.Date) + " / " + str(self.Time))

    class Meta:
        verbose_name = "4 - Clients Booked call"
        verbose_name_plural = "4 - Clients Booked call"

class Designguide(models.Model):
    label = models.CharField(max_length=256, blank=True, null=True)
    design = models.FileField(upload_to='static/design_guide')

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "5 - Design Guide Template"
        verbose_name_plural = "5 - Design Guide Templates"
