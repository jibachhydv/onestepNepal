from django.shortcuts import render

# Create your views here.
def readNepal(request):


    # rendering readnepal.html
    return render(request, 'readNepal/readnepal.html', {
        
    })