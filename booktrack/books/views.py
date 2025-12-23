from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book, UserBook, User

# Спеціальна форма для твоєї моделі користувача
class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email") # Додаємо імейл, як ти хотіла в моделях

def catalog_view(request):
    books = Book.objects.all()
    if request.user.is_authenticated and 'add' in request.GET:
        book_id = request.GET.get('add')
        status = request.GET.get('status')
        book = get_object_or_404(Book, id=book_id)
        UserBook.objects.update_or_create(
            user=request.user, book=book, defaults={'status': status}
        )
        return redirect('home')
    return render(request, "main.html", {"books": books})

def book_detail(request, book_id):
    # Шукаємо книгу за ID, якщо не знайдемо — покажемо помилку 404
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def profile_view(request):
    ub = UserBook.objects.filter(user=request.user)
    return render(request, "profile.html", {
        "wishlist": ub.filter(status='wishlist'),
        "reading": ub.filter(status='reading'),
        "read": ub.filter(status='read'),
    })

def register_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST) # Використовуємо нашу виправлену форму
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else: 
        form = MyUserCreationForm()
    return render(request, 'register.html', {'form': form})