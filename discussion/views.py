from django.shortcuts import render
from .models import Discussion
from django.http import Http404
# Create your views here.
def questionlist(request):
    questions = Discussion.objects.all()

    return render(request, 'discussion/questionlist.html', {
        'questions': questions,
    })

def questiondetail(request, id):

    try:
        question = Discussion.objects.get(pk=id)
    except Discussion.DoesNotExist or Discussion.MultipleObjectsReturned:
        raise Http404("Do Such Question Exist")

    return render(request, 'discussion/questiondetail.html', {
        'question': question
    })

