from django.shortcuts import render
from guest_book.models import GuestBook


def guest_book_view(request):
    guest_book_list = GuestBook.objects.filter(status='active').order_by('-created_at')
    context = {
        'guest_book_list': guest_book_list
    }
    return render(request, 'guest_book_list_page.html', context=context)