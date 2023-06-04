from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=360)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=350)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book')
    description = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def get_absolute_url(self):
        return reverse("book_details", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text