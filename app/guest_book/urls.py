from django.urls import path

from guest_book.views.guest_book import *

urlpatterns = [
    path('', guest_book_view),
    path('guest_book/', guest_book_view, name='guest_book_list'),
    path('guest_book/<int:pk>/update', guest_record_update, name='guest_record_update')
]