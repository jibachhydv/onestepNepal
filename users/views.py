from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth import login as account_login
from django.contrib.auth import logout as account_logout

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

# Password reset

