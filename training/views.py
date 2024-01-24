from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import generic
from training.models import Book
from rest_framework.permissions import IsAdminUser

def home(request):
    return HttpResponse('Hello, World!')


class BookLisView(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    # permission_classes = [IsAdminUser]