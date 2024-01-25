from django_filters import rest_framework as filters
from training.models import Book


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(method='find_book')
    class Meta:
        model = Book
        fields = ['name', 'publisher']
        
    def find_book(self, queryset, name, value):
        query = {"{}__icontains".format(name):value}
        queryset = queryset.filter(**query)
        return queryset