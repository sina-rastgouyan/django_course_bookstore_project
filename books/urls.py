from django.urls import path

from . import views
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('new/', views.BookCreateView.as_view(), name='book_cration'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
]