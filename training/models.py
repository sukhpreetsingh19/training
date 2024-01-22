from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Book(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    publisher = models.CharField(_("Publisher"), max_length=50)
    price = models.FloatField(_("price"))
    
    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"