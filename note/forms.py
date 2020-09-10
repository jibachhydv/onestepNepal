from django.forms import ModelForm

from .models import Note

class NewNoteForm(ModelForm):

    class Meta:
        model = Note
        fields = [
            'title',
            'content',
            'grade',
            'subject',
        ]