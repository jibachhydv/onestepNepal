from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import CurrentBook, Participiant
from django.http import HttpResponseRedirect

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
@login_required
def addBook(request):

  if request.method == "POST":
    # Reader name
    reader = request.user

    # book 
    book = CurrentBook.objects.get(id=request.POST['bookId'])

    # Add Participiant
    Participiant.objects.create(reader=reader, bookName=book, dateStarted=datetime.now(), doneReading=False)

    book.reader.add(request.user)
    
    # Redirect to the same page
    return redirect(request.META['HTTP_REFERER'])

  else:
    return HttpResponseRedirect(reverse('homepage'))