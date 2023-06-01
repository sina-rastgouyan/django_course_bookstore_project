from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm

# Create your views here.
class BookListView(generic.ListView):
    model= Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model= Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_creation.html'
    fields = ['title', 'description', 'author', 'price']
    success_url = reverse_lazy('book_list')

class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_detail_update.html'
    
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/delete_book_ensurement.html'
    success_url = reverse_lazy('book_list')