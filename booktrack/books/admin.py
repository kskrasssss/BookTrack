from django.contrib import admin
from .models import Book, UserBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'price')
    search_fields = ('title',)


@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'rating')
    list_filter = ('status', 'rating')
