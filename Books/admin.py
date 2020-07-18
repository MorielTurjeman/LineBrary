from django.contrib import admin
from .models import Book , BookStationRelation , Order, AddBook
#from .models import Book , BookStationRelation , Order , Profile

# Register your models here.

admin.site.register(Book)
admin.site.register(BookStationRelation)
admin.site.register(Order)
admin.site.register(AddBook)
#admin.site.register(Profile)