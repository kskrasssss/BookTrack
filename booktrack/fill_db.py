import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booktrack.settings')
django.setup()

from books.models import Book

data = [
    {"t": "Афон 2643", "a": "Нільс Вестербоер", "p": 650, "i": "https://static.yakaboo.ua/media/catalog/product/f/i/file_330_2.jpg", "y": 2023},
    {"t": "У темряві. Світло згасло", "a": "Навесса Аллен", "p": 420, "i": "https://static.yakaboo.ua/media/cloudflare/product/webp/600x840/d/4/d4bbc9edbf452170e661e4ee2458bb60.jpg", "y": 2024},
    {"t": "Нічний трунок", "a": "Алекс Астер", "p": 570, "i": "https://static.yakaboo.ua/media/catalog/product/6/3/635ef7c2_nichnyi-trunok.webp", "y": 2024},
    {"t": "Нові Темні Віки. Колапс", "a": "Макс Кідрук", "p": 699, "i": "https://static.yakaboo.ua/media/catalog/product/_/_/____01_cr.jpg", "y": 2023},
    {"t": "Midnight at the Christmas Bookshop", "a": "Дженні Колґан", "p": 655, "i": "https://static.yakaboo.ua/media/catalog/product/6/1/61obfwdxzwl._sl1000_.jpg", "y": 2023},
    {"t": "A Body at the Christmas Book Fair", "a": "Хелен Кокс", "p": 1664, "i": "https://static.yakaboo.ua/media/catalog/product/9/7/9781529442175_0.jpg", "y": 2022},
    {"t": "The Merry Christmas Project", "a": "Кеті Бремлі", "p": 756, "i": "https://static.yakaboo.ua/media/catalog/product/6/1/61dbrg61a3l._sl1000_.jpg", "y": 2021},
    {"t": "The Christmas Fix", "a": "Люсі Скор", "p": 539, "i": "https://static.yakaboo.ua/media/catalog/product/9/7/9781399735537_0.jpg", "y": 2023},
    {"t": "Хто зробить сніг", "a": "Т. Прохасько, М. Прохасько", "p": 79, "i": "https://static.yakaboo.ua/media/catalog/product/f/i/file_215_2.jpg", "y": 2013},
    {"t": "Диво-лижі ведмедика Пухнастика", "a": "Марія Пономаренко", "p": 50, "i": "https://static.yakaboo.ua/media/catalog/product/9/7/978-966-10-8401-7.jpg", "y": 2020},
    {"t": "Шоколадний Kіт і Цукеркова Відьма", "a": "Тетяна Стрижевська", "p": 420, "i": "https://static.yakaboo.ua/media/cloudflare/product/webp/600x840/1/_/1_75_19.jpg", "y": 2023},
    {"t": "Емі і таємний клуб супердівчат", "a": "Агнєшка Мєлех", "p": 120, "i": "https://static.yakaboo.ua/media/cloudflare/product/webp/600x840/e/m/emi_ida_swieta_cover6.jpg", "y": 2022}
]

for item in data:
    Book.objects.get_or_create(
        title=item['t'], 
        defaults={
            'author': item['a'], 
            'price': item['p'], 
            'image_url': item['i'], 
            'year': item['y'],
            'rating': 5,  # ДОДАЛИ РЕЙТИНГ
            'description': 'Опис книги'
        }
    )

print("--- ВСЕ! ТЕПЕР ПОВИННО ПРАЦЮВАТИ ---")