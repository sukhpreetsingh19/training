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
from django_filters.rest_framework import DjangoFilterBackend
from training.filters import BookFilter

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
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    # search_fields = ['name',]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # params = self.request.query_params
        # name = params.get('name',None)
        # if name:
        #     queryset = queryset.filter(name=name)
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
