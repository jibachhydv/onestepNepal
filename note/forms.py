from django.forms import ModelForm

from .models import Note

from django_summernote.widgets import SummernoteWidget

from django.core.exceptions import ValidationError

class NewNoteForm(ModelForm):

    class Meta:
        model = Note
        fields = [
            'title',
            'content',
            'grade',
            'subject',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
    
