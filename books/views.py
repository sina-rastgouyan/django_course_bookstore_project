from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm, CommentForm

# Create your views here.
class BookListView(generic.ListView):
    model= Book
    template_name = 'books/book_list.html'
    paginate_by = 8
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):
#     model= Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    #get book comments
    book_comments = book.comment.all()
    # Comment Form
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'book': book,
        'comments':book_comments,
        'comment_form': comment_form
    }
    
    return render(request, 'books/book_detail.html', context)

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_creation.html'
    fields = ['title', 'description', 'author', 'price', 'cover']
    success_url = reverse_lazy('book_list')

class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_detail_update.html'
    
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/delete_book_ensurement.html'
    success_url = reverse_lazy('book_list')