from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=350)
    description = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title