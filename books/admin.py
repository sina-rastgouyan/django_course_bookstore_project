from django.contrib import admin

from .models import Book
# Register your models here.

class CustomBooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']

admin.site.register(Book, CustomBooksAdmin)