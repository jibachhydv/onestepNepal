from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Note

from django.contrib.auth.mixins import LoginRequiredMixin

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/notelist.html'

class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'note/notedetail.html'

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'note/newnote.html'
    fields = [
        'title',
        'content',
        'grade',
        'subject',
    ]
    
    class Meta:
        widgets = {
            'content': SummernoteWidget(),
        }

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)