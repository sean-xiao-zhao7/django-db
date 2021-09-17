from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(req):
    books = Book.objects.all().order_by('title')
    total = books.count()
    average_rating = books.aggregate(Avg('rating'))
    return render(req, 'index.html', {"books": books, "total": total, "average_rating": average_rating,})

def book_details(req, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(req, 'book_details.html', {
        'title': book.title,
        'author': book.author,
        'is_best_selling': book.is_best_selling,
        'content': book.content,
        'rating': book.rating,
    })