from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CurrentBook, Participiant

from datetime import datetime


# Create your views here.
def readNepal(request):

    # Current Month of the Year
    currentMonth = datetime.now().month

    # Book Of the Month
    bookOfTheMonth = CurrentBook.objects.all().filter(date__month=currentMonth)[:2]

    # rendering readnepal.html
    return render(request, 'readNepal/readnepal.html', {
      'books': bookOfTheMonth,  
    })

def testHomePage(request):
    return render(request, 'test/test.html', {
        
    })


# Add Book