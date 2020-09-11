from django.shortcuts import render, reverse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Note

from django.contrib.auth.mixins import LoginRequiredMixin

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.contrib.auth.decorators import login_required

from .forms import NewNoteForm

from django.http import HttpResponse, HttpResponseRedirect

class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/notelist.html'

class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'note/notedetail.html'
    

@login_required()
def createNote(request):

    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(status='published', 
                                title=form.cleaned_data['title'],
                                author=request.user,
                                content=form.cleaned_data['content'],
                                subject=form.cleaned_data['subject'],
                                grade=form.cleaned_data['grade'])

            return HttpResponseRedirect(reverse('notelist'))

    form = NewNoteForm()
    return render(request, 'note/newnote.html', {
        'form': form
    })
