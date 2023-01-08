from django.shortcuts import render


# Create your views here.

rooms = [

    {id:'1', 'name': 'Lets learn python'},
    {id:'2', 'name': 'Design with me'},
    {id:'1', 'name': 'Frontend devs'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html',context) # Now we can use render # as we have added rooms list in home functions so we would only be able to add them to home.html not room 
    # return HttpResponse('Home page')
    
def room(request):    
    return render(request, 'room.html')
    # return HttpResponse('ROOM')