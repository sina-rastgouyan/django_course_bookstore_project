from django.contrib import admin

from .models import Book, Author
# Register your models here.

class CustomBooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Book, CustomBooksAdmin)