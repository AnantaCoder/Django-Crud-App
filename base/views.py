from django.shortcuts import render , redirect
# from django.http import HttpResponse
from django.db.models import Q
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1, 'name':'lets learn python'},
#     {'id':2, 'name':'lets learn java'},
#     {'id':3, 'name':'lets learn c++'}
# ]



from django.db.models import Q

def home(request):
    query = request.GET.get('q')  # Get the search query from the URL
    rooms = Room.objects.all()

    if query:
        # Filter rooms based on the query (name, topic, or host)
        rooms = rooms.filter(
            Q(name__icontains=query) |
            Q(topic__name__icontains=query) |
            Q(host__username__icontains=query)
        )

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id = pk , )
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save() # saving if all goof 
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'base/room_form.html' , context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    # Fix the typo here: change 'from' to 'form'
    context = {'form': form}  # Corrected key name
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)  # Corrected: Use `id=pk` instead of just `pk`
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

