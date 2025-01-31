from django.shortcuts import render , redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from .models import Room , Topic
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1, 'name':'lets learn python'},
#     {'id':2, 'name':'lets learn java'},
#     {'id':3, 'name':'lets learn c++'}
# ]



from django.db.models import Q




def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request, "This user does not  exists ")
            
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
    context = {}
    return render(request, 'base/login_register.html' , context)



def logoutUser(request):
    logout(request)
    return redirect('home')






def home(request):
    query = request.GET.get('q')  # Get the search query from the URL
    rooms = Room.objects.all()

    if query:
        # Filter rooms based on the query (name, topic, or host)
        rooms = rooms.filter(
            Q(name__icontains=query) |
            Q(topic__name__icontains=query) |
            Q(host__username__icontains=query) |
            Q(description__icontains=query)
        )

    topics = Topic.objects.all()  # Fetch all topics
    room_count = rooms.count()

    context = {
        'rooms': rooms,
        'room_count': room_count,
        'topics': topics,  # Pass topics to the template
    }
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id = pk , )
    context = {'room':room}
    return render(request, 'base/room.html', context)

@login_required(login_url='login') # ensures only user with ids logged in 
def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save() # saving if all goof 
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'base/room_form.html' , context)

@login_required(login_url='login') # ensures only user with ids logged in 
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user!= room.user:
        return HttpResponse('You do not own this room')
    
    
    
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

        
    if request.user!= room.user:
        return HttpResponse('You do not own this room')

        
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

