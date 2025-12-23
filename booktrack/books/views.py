from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Book, UserBook, User
from .models import CartItem

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

def catalog_view(request):
    books = Book.objects.all()
    
    # Логіка додавання/зміни статусу
    if request.user.is_authenticated and 'add' in request.GET:
        book_id = request.GET.get('add')
        status = request.GET.get('status')
        book = get_object_or_404(Book, id=book_id)
        
        # update_or_create знайде існуючу книгу користувача і змінить статус 
        # (наприклад, з 'wishlist' на 'read')
        UserBook.objects.update_or_create(
            user=request.user, 
            book=book, 
            defaults={'status': status}
        )
        return redirect('profile')
        
    return render(request, "main.html", {"books": books})

@login_required
def delete_from_list(request, item_id):
    # Видаляємо саме запис UserBook
    item = get_object_or_404(UserBook, id=item_id, user=request.user)
    item.delete()
    return redirect('profile')

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def profile_view(request):
    ub = UserBook.objects.filter(user=request.user).select_related('book')
    return render(request, "profile.html", {
        "wishlist": ub.filter(status='wishlist'),
        "reading": ub.filter(status='reading'),
        "read": ub.filter(status='read'),
    })

def register_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else: 
        form = MyUserCreationForm()
    return render(request, 'register.html', {'form': form})


# Функції кошика

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, 
        book=book,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    # Знаходимо товар у кошику саме цього користувача
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

@login_required
def checkout_view(request):
    # Тут ми просто очищаємо кошик, імітуючи успішну оплату
    CartItem.objects.filter(user=request.user).delete()
    return render(request, 'payment_success.html')