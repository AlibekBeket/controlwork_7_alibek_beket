from django.urls import path

from guest_book.views.guest_book import guest_book_view

urlpatterns = [
    path('', guest_book_view, name='guest_book_list'),
    path('guest_book/', guest_book_view, name='guest_book_list')
]