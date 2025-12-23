from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.catalog_view, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('delete-item/<int:item_id>/', views.delete_from_list, name='delete_from_list'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/checkout/', views.checkout_view, name='checkout'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

]