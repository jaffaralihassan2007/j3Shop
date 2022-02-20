from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    Describe = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photo/%y/%m/%d', verbose_name="photo")

    def __str__(self):
        return self.name