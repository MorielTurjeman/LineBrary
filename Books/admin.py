from django.contrib import admin
from .models import Book , BookStationRelation , Order, Contributions
#from .models import Book , BookStationRelation , Order , Profile

# Register your models here.

admin.site.register(Book)
admin.site.register(BookStationRelation)
admin.site.register(Order)
admin.site.register(Contributions)
#admin.site.register(Profile)