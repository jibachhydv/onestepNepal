from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CurrentBook, Participiant

from datetime import datetime
import calendar

# Create your views here.
def readNepal(request):

    # Current Month of the Year
    currentMonth = datetime.now().month

    # Book Of the Month
    bookOfTheMonth = CurrentBook.objects.all().filter(date__month=currentMonth).filter(isItCurrentBook=True)[:2]

    # Participiant
    participiants = Participiant.objects.all().filter(dateStarted__month=currentMonth)

    # rendering readnepal.html
    return render(request, 'readNepal/readnepal.html', {
      'books': bookOfTheMonth,
      'monthName': calendar.month_name[currentMonth],
      'readers': participiants,
    })

def testHomePage(request):
    return render(request, 'test/test.html', {
        
    })


# Add Book