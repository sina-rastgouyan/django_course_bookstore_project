from django.urls import path

from . import views
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    # path('<int:pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('<int:pk>/', views.book_detail_view, name='book_details'),
    path('new/', views.BookCreateView.as_view(), name='book_creation'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book')
]