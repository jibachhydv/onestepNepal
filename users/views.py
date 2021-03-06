from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from .models import User
from django.core.mail import EmailMessage

from django.contrib.auth.tokens import default_token_generator


from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model

from note.models import *
from discussion.models import Discussion
from extrapp.models import *

from datetime import datetime


def homepage(request):

    # Reccommended Posts
    if request.user.is_authenticated:
        recNotes = Note.published.all().exclude(
            author=request.user).order_by('-views', 'likes')[:4]
    else:
        recNotes = Note.published.all()[:4]
    print(recNotes)

    # Recommended Question
    recQuestions = Discussion.objects.all().exclude(answered_status=True)[:4]
    print(recQuestions)


     # Current Month of the Year
    currentMonth = datetime.now().month

    # Book Of the Month
    bookOfTheMonth = CurrentBook.objects.all().filter(date__month=currentMonth).filter(isItCurrentBook=True)[:2]

    return render(request, 'base.html', {
        'recommendedNotes': recNotes,
        'recommendedQuestion': recQuestions,
        'books': bookOfTheMonth,
        # 'doneReading': doneReading(request.user, bookOfTheMonth)
    })


def login(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                account_login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return render(request, 'account/account_not_activated.html', {

                })
        else:
            return render(request, 'account/login.html', {
                'error': True
            })
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('homepage'))
        return render(request, "account/login.html")


def logout(request):
    account_logout(request)
    return HttpResponseRedirect(reverse("homepage"))


# Password Change
class PasswordChangeView(PasswordChangeView):
    template_name = 'account/passwordchange.html'

# Password Change Done


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'account/passwordchangedone.html'

# Password reset view


class PasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_email.html'

# Password Reset Done View


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    extra_context = {

    }


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


# Profile
def profile(request, id, username):

    try:
        user = User.objects.get(pk=id, username=username)
    except User.DoesNotExist:
        return HttpResponse("No Such User")

    return render(request, 'profile/profile.html', {
        'user': user
    })

# User registration


def signup(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('homepage'))

    if request.method == 'GET':
        return render(request, 'registration/signup.html')

    if request.method == 'POST':
        email_address = request.POST["email"]
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        if request.POST['profilePicture']:
            havePhoto = True
        else:
            havePhoto = False
        # photo = request.POST['profilePicture']

        # Ensure that password matches
        if len(password1) < 8 or len(password2) < 8:
            return render(request, 'registration/signup.html', {
                "error_message": "Password cannot be shorter than 8 digits"
            })

        if password1 != password2:
            return render(request, 'registration/signup.html', {
                "error_message": "Passwords don't match",
            })

        # Attempt to create a new user
        try:
            if havePhoto:
                user = User.objects.create_user(username=username,
                                                first_name=first_name, last_name=last_name,
                                                email=email_address, password=password2,
                                                photo=request.POST['profilePicture'])
            else:
                user = User.objects.create_user(username=username,
                                                first_name=first_name, last_name=last_name,
                                                email=email_address, password=password2)
            user.is_active = False
            user.save()

        except IntegrityError as e:
            print(e)
            return render(request, 'registration/signup.html', {
                "error_message": "Email Address Already Taken"
            })

        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('registration/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = email_address
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return render(request, 'account/account_confirmation.html', {

        })


UserModel = get_user_model()


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'account/account_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')
