from django.shortcuts import render, get_object_or_404, redirect

from .forms import RoomForm
from .models import Room


# Create your views here.
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some-view-to-redirect')  # Redirigez vers une vue appropriée
    else:
        form = RoomForm()
    return render(request, 'room/create_room.html', {'form': form})


def update_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('some-view-to-redirect')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room/update_room.html', {'form': form, 'room': room})


def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    room.delete()
    return redirect('some-view-to-redirect')


def get_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'room/room_detail.html', {'room': room})


def get_all_room(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms_list.html', {'rooms': rooms})
