from django.shortcuts import render, reverse, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Note, Comment

from django.contrib.auth.mixins import LoginRequiredMixin

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.contrib.auth.decorators import login_required

from .forms import NewNoteForm

from django.http import HttpResponse, HttpResponseRedirect, Http404



class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/notelist.html'

def notelist(request):
    notes = Note.published.all()
    return render(request, 'note/notelist.html', {
        'notes': notes,
    })

""" class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'note/notedetail.html'

    """

def notedetail(request, pk, slug):

    try:
        note = Note.objects.get(id=pk, slug=slug)
    except Note.DoesNotExist:
        return HttpResponse("Such Note Doesnot exist")
    comments = note.comments.all()

    note.increaseView()
    note.save()
    print(note.views)
    return render(request, 'note/notedetail.html', {
        'note': note,
        'comments': comments,
    })


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

class NoteUpdateView(UpdateView, LoginRequiredMixin):
    model = Note
    template_name = 'note/noteupdate.html'
    form_class = NewNoteForm
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(NoteUpdateView, self).dispatch(request, *args, **kwargs)

@login_required
def noteDelete(request, pk, slug):

    try:
        note = Note.objects.get(pk=pk, slug=slug)
    except Note.DoesNotExist:
        return HttpResponse("Such Post Doesnot exist")
        
    if request.user != note.author:
        return Http404("You are not allowed to delete the post")
        
    note.status = 'draft'
    note.save()
    return HttpResponseRedirect(reverse('notelist'))


@login_required
def newcomment(request, noteid):

    if request.method == "POST":
        comment = request.POST.get('newcomment')
        if (comment == ''):
            return redirect(request.META['HTTP_REFERER'])
        note = Note.objects.get(pk=noteid)
        user = request.user
        Comment.objects.create(post=note, comment_by=user, comment=comment)
        return redirect(request.META['HTTP_REFERER'])
    
@login_required
def deletecomment(request, commentid):

    try:
        comment = Comment.objects.get(pk=commentid)
    except Comment.DoesNotExist or Comment.MultipleObjectsReturned:
        raise Http404("Not allowded")

    comment.delete()
    return redirect(request.META['HTTP_REFERER'])