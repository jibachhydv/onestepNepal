from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from .models import User

def homepage(request):
    return render(request, 'base.html')


def login(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                account_login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("Your account has been disabled")
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
def profile(request,id):
    
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponse("No Such User")
    
    return render(request, 'profile/profile.html', {
        'user': user
    })
    