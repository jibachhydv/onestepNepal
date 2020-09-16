from django_summernote.fields import SummernoteTextFormField

from django.forms import ModelForm

from .models import Discussion, Answer

from django_summernote.widgets import SummernoteWidget


class AskForm(ModelForm):

    # question = SummernoteTextFormField(label='Question Description')

    class Meta:
        model = Discussion
        fields = [
            'title',
            'grade',
            'subject',
            'detail',
        ]

        widgets = {
            'detail': SummernoteWidget(),
        }

class QuestionAnswer(ModelForm):

    class Meta:
        model = Answer
        fields = [
            'answer',
        ]

        widgets = {
            'answer': SummernoteWidget(),
        }

    
