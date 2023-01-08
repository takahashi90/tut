from django.shortcuts import render


# Create your views here.

rooms = [

    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend devs'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html',context) # Now we can use render # as we have added rooms list in home functions so we would only be able to add them to home.html not room 
    
    
def room(request, pk):
    room = None    
    for i in rooms:
        if i['id'] == int(pk):
            room = i  
    context = {'room': room}
    return render(request, 'base/room.html', context)  # we will have to specify path for our room and home html files because they are inside our app 