from django.contrib import admin

from guest_book.models import GuestBook


# Register your models here.
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ("id", "author_name", "author_email", "text", "created_at", "updated_at", "status")
    list_filter = ("id", "author_name", "author_email", "text", "created_at", "updated_at", "status")
    search_fields = ("id", "author_name", "author_email", "text", "status")
    fields = ("author_name", "author_email", "text", "created_at", "updated_at", "status")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(GuestBook, GuestBookAdmin)
