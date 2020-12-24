from django.db import models
from django.core.validators import MinValueValidator


                          
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
        verbose_name = "1 - Orders Table"
        verbose_name_plural = "1 - Orders Table"

class CustomerData(models.Model):
    Name = models.CharField(null=False, max_length=1024)
    Email = models.CharField(null=False, max_length=1024)
    Cell = models.CharField(null=False, max_length=20)
    Address = models.CharField(null=False, max_length=2048)
    Orders = models.ManyToManyField(Orders)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = "2 - Customer Information"
        verbose_name_plural = "2 - Customer Information"

