from django.urls import path

from guest_book.views.guest_book import *

urlpatterns = [
    path('', guest_book_view),
    path('guest_book/', guest_book_view, name='guest_book_list'),
    path('guest_book/<int:pk>/update', guest_record_update, name='guest_record_update'),
    path('guest_book/<int:pk>/delete', guest_record_delete, name='guest_record_delete'),
    path('guest_book/<int:pk>/confirm_delete', guest_record_confirm_delete, name='guest_record_confirm_delete')
]