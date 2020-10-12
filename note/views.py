from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, reverse, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Note, Comment

from django.contrib.auth.mixins import LoginRequiredMixin

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.contrib.auth.decorators import login_required

from .forms import NewNoteForm

from django.http import HttpResponse, HttpResponseRedirect, Http404

import re

class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note/notelist.html'


def notelist(request):
    # Get all the published notes
    notes = Note.published.all()

    # Show five notes per page
    paginator = Paginator(notes, 10)

    # Get the current page number
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'note/notelist.html', {
        'page_obj': page_obj,
    })


""" class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'note/notedetail.html'

    """


def notedetail(request, pk, slug):

    try:
        note = Note.published.get(id=pk, slug=slug)
    except Note.DoesNotExist:
        return HttpResponse("Such Note Doesnot exist")
    comments = note.comments.all()

    note.increaseView()
    note.save()

    # List of Related Post
    relatedPost = []

    # List of Excluded Post
    excludePost = []
    excludePost.append(note.id)

    # Post from Same User if available else random page
    sameUserNote = Note.published.filter(
        author=note.author).exclude(id__in=excludePost)
    if len(sameUserNote) >= 1:
        relatedPost.append(sameUserNote[0])
        excludePost.append(sameUserNote[0].id)
    else:
        relatedPost.append(Note.published.all().exclude(
            id__in=excludePost).order_by('-views')[0])
        excludePost.append(Note.published.all().exclude(
            id__in=excludePost).order_by('-views')[0].id)

    # Post from same subject if available
    sameSubjectNote = Note.published.filter(
        subject=note.subject).exclude(id__in=excludePost)
    if len(sameSubjectNote) >= 1:
        relatedPost.append(sameSubjectNote[0])
        excludePost.append(sameSubjectNote[0].id)
    else:
        relatedPost.append(Note.published.all().exclude(
            id__in=excludePost).order_by('-views')[0])
        excludePost.append(Note.published.all().exclude(
            id__in=excludePost).order_by('-views')[0].id)

    # Post with most views
    mostViewedPost = Note.published.all().order_by(
        '-views').exclude(id__in=excludePost)
    if len(mostViewedPost) >= 1:
        relatedPost.append(mostViewedPost[0])
        excludePost.append(mostViewedPost[0].id)
    else:
        relatedPost.append(Note.published.all().exclude(
            id__in=excludePost).order_by('-views')[0])
        excludePost.append(Note.published.all().exclude(
            id__in=excludePost).order_by('-views')[0].id)

    # print(relatedPost)
    return render(request, 'note/notedetail.html', {
        'note': note,
        'comments': comments,
        'relatedNotes': relatedPost,
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

from itertools import chain


# Search Box
def searchAll(request):

    searchQuery = request.GET.get('q')
    # print(f"Search Query Is {searchQuery}")

    # wordList = re.sub("[^\w]", " ",  searchQuery).split()
    # print(wordList)

    # Similar Notes
    similarTitle = Note.published.all().filter(
        title__contains=searchQuery).order_by('-views', '-likes')
    print(f"Similar post bt title are: {similarTitle}")
    excludedNotes = [note.id for note in similarTitle]

    similarContent = Note.published.all().filter(content__contains=searchQuery).order_by(
        '-views', '-likes').exclude(id__in=excludedNotes)

    searchNotes = list(chain(similarTitle, similarContent))
    
    # Search Result
    return render(request, 'note/searchresult.html', {
        'searchNotes': searchNotes,
        'query': searchQuery,
    })


# Search Result by Subject
def searchSubject(request, subject):

    searchNotes = Note.published.all().filter(
        subject=subject
    ).order_by('-views', '-likes')

    # Search Result
    return render(request, 'note/searchresult.html', {
        'searchNotes': searchNotes,
        'query': subject,
    })

# Search Result by grade
def searchGrade(request, grade):

    searchNotes = Note.published.all().filter(
        grade=grade
    ).order_by('-views', '-likes')

    # Search Result
    return render(request, 'note/searchresult.html', {
        'searchNotes': searchNotes,
        'query': grade,
    })