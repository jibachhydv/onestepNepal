from django.contrib import admin

from .models import CurrentBook, OtherBook

# Register your models here.
admin.site.register(CurrentBook)
admin.site.register(OtherBook)