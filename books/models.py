from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.CharField(max_length=350)
    description = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def get_absolute_url(self):
        return reverse("book_details", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title