from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("book-details/<slug:slug>", views.book_details, name="book-details"),
]
