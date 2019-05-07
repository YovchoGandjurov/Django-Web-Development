from django.shortcuts import render
from django.views import generic
from .models import Book, Author


class BookView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
