from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from training.serializers import BooksSerializer
from training.models import Book


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

class Booklist(generics.ListCreateAPIView):
    queryset  = Book.objects.all()
    serializer_class = BooksSerializer


