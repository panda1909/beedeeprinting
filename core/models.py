from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file_extension

                          
class Orders(models.Model):
    OrderId = models.CharField(null=False, max_length=256)
    Product_name = models.CharField(null=False, max_length=512, default='pd')
    Customer = models.CharField(null=False, max_length=512)
    Delivery_address = models.CharField(null=False, max_length=512, default='pd')
    Contact = PhoneNumberField()
    Email = models.EmailField(max_length=254)
    Delivery_date = models.DateField( auto_now=False, auto_now_add=False)
    Status = models.CharField(null=False, max_length=256)
    Quantity = models.PositiveIntegerField(default=1, blank=False, editable=True)
    Size = models.CharField(null=False, max_length=1024)
    Price = models.FloatField(default=0, blank=False, editable=True, validators=[MinValueValidator(0.1)])
    Template = models.FileField(upload_to='static/Order_templates', max_length=256, validators=[validate_file_extension])

    def __str__(self):
        return str(self.OrderId)

    class Meta:
        verbose_name = "1 - Orders Table"
        verbose_name_plural = "1 - Orders Table"

class CustomerData(models.Model):
    Name = models.CharField(null=False, max_length=1024)
    Email = models.EmailField(max_length=254)
    Cell = PhoneNumberField()
    Address = models.CharField(null=False, max_length=2048)
    Orders = models.ManyToManyField(Orders)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = "2 - Customer Information"
        verbose_name_plural = "2 - Customer Information"

