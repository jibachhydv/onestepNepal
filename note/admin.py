from django.contrib import admin
from .models import Note


from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class NoteAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


admin.site.register(Note,NoteAdmin)