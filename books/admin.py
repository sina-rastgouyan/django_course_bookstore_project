from django.contrib import admin

from .models import Book, Author, Comment
# Register your models here.

class CustomBooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_time_created', 'book', 'text','is_active', 'recommend']
    list_editable = ['is_active', 'recommend']
admin.site.register(Book, CustomBooksAdmin)