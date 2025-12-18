from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(8)]  
    )

    def __str__(self):
        return self.email


class Book(models.Model):
    GENRE_CHOICES = [
        ('novel', 'Роман'),
        ('story', 'Повість'),
        ('tale', 'Оповідання'),
        ('novella', 'Новела'),
        ('epic', 'Епос'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.price} грн)"

class ReadingStatus(models.TextChoices):
    WISHLIST = 'wishlist', 'Хочу прочитати'
    READING = 'reading', 'Читаю'
    READ = 'read', 'Прочитано'


class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ReadingStatus.choices)
    note = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'book') 

    def __str__(self):
        return f"{self.user.email} — {self.book.title} ({self.status})"
