from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

class Book(models.Model):
    GENRE_CHOICES = [
        ('novel', 'Роман'), ('story', 'Повість'), ('tale', 'Оповідання'),
        ('novella', 'Новела'), ('epic', 'Епос'),
    ]
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="Невідомий автор")
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1) # Загальний рейтинг
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500, blank=True) # Щоб не мучитись з файлами

    def __str__(self):
        return self.title

class UserBook(models.Model):
    STATUS_CHOICES = [
        ('wishlist', 'Хочу прочитати'),
        ('reading', 'Читаю'),
        ('read', 'Прочитано'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user_rating = models.IntegerField(default=0) # Особиста оцінка

    class Meta:
        unique_together = ('user', 'book')

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.book.price * self.quantity