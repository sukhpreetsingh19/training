from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from training.serializers import BooksSerializer
from training.models import Book
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from projectpipedit.custompermission import IsSuperuser

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

class Booklist(generics.ListCreateAPIView):
    queryset  = Book.objects.all().order_by('id')
    serializer_class = BooksSerializer
    # authentication_classes= [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsSuperuser]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name',]
