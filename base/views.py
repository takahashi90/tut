from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html') # Now we can use render 
    # return HttpResponse('Home page')
    
def room(request):    
    return render(request, 'room.html')
    # return HttpResponse('ROOM')