from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from guest_book.models import GuestBook

from guest_book.forms import *


def guest_book_view(request):
    guest_book_list = GuestBook.objects.filter(status='active').order_by('-created_at')
    form = GuestBookForm()
    form_find = GuestFind()
    if not request.POST:
        context = {
            'guest_book_list': guest_book_list,
            'form': form,
            'form_find': form_find
        }
        return render(request, 'guest_book_list_page.html', context=context)
    if request.POST.get('name'):
        form_find = GuestFind(data=request.POST)
        if not form_find.is_valid():
            context = {
                'guest_book_list': guest_book_list,
                'form_find': form_find,
                'form': form
            }
            return render(request, 'guest_book_list_page.html', context=context)
        else:
            guest_book_list = GuestBook.objects.filter(status='active', author_name=request.POST.get('name')).order_by('-created_at')
            context = {
                'guest_book_list': guest_book_list,
                'form_find': form_find,
                'form': form,
                'return_post_find_name': True
            }
            return render(request, 'guest_book_list_page.html', context=context)
    form = GuestBookForm(data=request.POST)
    if not form.is_valid():
        context = {
            'guest_book_list': guest_book_list,
            'form_find': form_find,
            'form': form
        }
        return render(request, 'guest_book_list_page.html', context=context)
    else:
        GuestBook.objects.create(**form.cleaned_data)
        return redirect(reverse('guest_book_list'))


def guest_record_update(request, pk):
    guest_record = get_object_or_404(GuestBook, pk=pk)
    if not request.POST:
        guest_record_dict = {
            'author_name': guest_record.author_name,
            'author_email': guest_record.author_email,
            'text': guest_record.text
        }
        form = GuestBookForm(data=guest_record_dict)
        context = {
            'guest_record': guest_record,
            'form': form
        }
        return render(request, 'guest_record_update.html', context=context)
    form = GuestBookForm(data=request.POST)
    if not form.is_valid():
        context = {
            'guest_record': guest_record,
            'form': form
        }
        return render(request, 'guest_record_update.html', context=context)
    else:
        guest_record.author_name = request.POST.get('author_name')
        guest_record.author_email = request.POST.get('author_email')
        guest_record.text = request.POST.get('text')
        guest_record.save()
        return redirect('guest_book_list')


def guest_record_delete(request, pk):
    guest_record = get_object_or_404(GuestBook, pk=pk)
    return render(request, 'guest_record_confirm_delete.html', context={'guest_record': guest_record})


def guest_record_confirm_delete(request, pk):
    guest_record = get_object_or_404(GuestBook, pk=pk)
    guest_record.delete()
    return redirect('guest_book_list')
