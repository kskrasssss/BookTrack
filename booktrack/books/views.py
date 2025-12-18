from django.shortcuts import render

books = [
    {"title": "Book 1", "author": "Author 1", "status": "want", "rating": 5, "notes": "Nice book"},
    {"title": "Book 2", "author": "Author 2", "status": "reading", "rating": 4, "notes": ""}
]

def catalog_view(request):
    want = [b for b in books if b["status"] == "want"]
    reading = [b for b in books if b["status"] == "reading"]
    done = [b for b in books if b["status"] == "done"]

    return render(request, "catalog.html", {
        "want": want,
        "reading": reading,
        "done": done
    })