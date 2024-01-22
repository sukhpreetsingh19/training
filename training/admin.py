from django.contrib import admin
from training.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    readonly_fields = ['price']
            

admin.site.register(Book, BookAdmin)