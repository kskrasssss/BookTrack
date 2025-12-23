from django.contrib import admin
from .models import Book, UserBook, User

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'year', 'price')
    search_fields = ('title', 'author')

@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
    # Використовуємо тільки ті поля, які є в моделі: user, book, status, user_rating
    list_display = ('user', 'book', 'status', 'user_rating')
    list_filter = ('status',)
    search_fields = ('user__username', 'book__title')

# Реєструємо користувача, щоб бачити його в адмінці
admin.site.register(User)