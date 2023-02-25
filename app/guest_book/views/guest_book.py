from django.shortcuts import render, redirect
from django.urls import reverse
from guest_book.models import GuestBook

from guest_book.forms import GuestBookForm


def guest_book_view(request):
    guest_book_list = GuestBook.objects.filter(status='active').order_by('-created_at')
    if not request.POST:
        form = GuestBookForm()
        context = {
            'guest_book_list': guest_book_list,
            'form': form
        }
        return render(request, 'guest_book_list_page.html', context=context)
    form = GuestBookForm(data=request.POST)
    if not form.is_valid():
        context = {
            'guest_book_list': guest_book_list,
            'form': form
        }
        return render(request, 'guest_book_list_page.html', context=context)
    else:
        GuestBook.objects.create(**form.cleaned_data)
        return redirect(reverse('guest_book_list'))