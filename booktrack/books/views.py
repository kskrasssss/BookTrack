from django.shortcuts import render

books = [
    {"title": "Book 1", "author": "Author 1", "status": "want", "rating": 5, "notes": "Nice book"},
    {"title": "Book 2", "author": "Author 2", "status": "reading", "rating": 4, "notes": ""}
]

def catalog_view(request):
    return render(request, "catalog.html", {"books": books})