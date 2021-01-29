from django.db import models

# Create your models here.

class Products(models.Model):
    Label = models.CharField(max_length=50,default='prod')
    Description = models.TextField(default='des',max_length=5000)
    image1 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)
    image2 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)
    image3 = models.ImageField(upload_to='static/Product_Images/Business_Cards/',max_length=None)

    def __str__(self):
        return(self.Label)

    class Meta:
        verbose_name = "Product List"
