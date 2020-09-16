from django.shortcuts import render
from .models import Discussion
from django.http import Http404
from .forms import AskForm, QuestionAnswer

# Create your views here.

def questionlist(request):
    questions = Discussion.objects.all()

    return render(request, 'discussion/questionlist.html', {
        'questions': questions,
        'askform': AskForm(),
    })

def questiondetail(request,slug,id):

    try:
        question = Discussion.objects.get(pk=id, slug=slug)

    except Discussion.DoesNotExist or Discussion.MultipleObjectsReturned:
        raise Http404("Do Such Question Exist")

    return render(request, 'discussion/questiondetail.html', {
        'question': question,
        'questionanswerform': QuestionAnswer(),
    })

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect

@login_required
def askquestion(request):

    if request.method == "POST":

        form = AskForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            grade = form.cleaned_data['grade']
            subject = form.cleaned_data['subject']
            detail = form.cleaned_data['detail']
            askedby = request.user


            # Save the question to the model
            Discussion.objects.create(title=title,grade=grade,subject=subject, detail=detail, askedby=askedby)

            return render(request, 'discussion/questionlist.html', {
                'questions': Discussion.objects.all()
            })
    
    else:
        form = AskForm()
        return render(request, 'discussion/askquestion.html', {
                'askform': form,
                'questions': Discussion.objects.all(),
            })
        
# Question Update View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class QuestionUpdateView(UpdateView, LoginRequiredMixin):

    model = Discussion
    template_name = 'discussion/updatequestion.html'
    form_class = AskForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.askedby != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(QuestionUpdateView, self).dispatch(request, *args, **kwargs)

from .models import Answer

@login_required
def newanswer(request, questionid):

    if request.method == "POST":
        form = QuestionAnswer(request.POST)

        if form.is_valid():

            answer = form.cleaned_data['answer']
            print(answer)

            # save the answer
            Answer.objects.create(answered_by=request.user, answer_on=Discussion.objects.get(pk=questionid), answer=answer)

            return redirect(request.META['HTTP_REFERER'])

from django.shortcuts import reverse

@login_required
def deletequestion(request, id):

    try:
        question = Discussion.objects.get(pk=id)
    except Discussion.DoesNotExist or Discussion.MultipleObjectsReturned:
        raise Http404("Not Allowded")

    question.delete()
    return HttpResponseRedirect(reverse('allquestions'))

   
@login_required
def deleteanswer(request, answerid):

    try:
        answer = Answer.objects.get(pk=answerid)
    except Answer.DoesNotExist or Answer.MultipleObjectsReturned:
        raise Http404("Not allowded")
    answer.delete()
    return redirect(request.META['HTTP_REFERER'])