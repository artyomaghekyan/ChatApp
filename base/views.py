from django.shortcuts import render, redirect
from .models import ChatRoom, ChatMessages

def index(request):
    rooms = ChatRoom.objects.all().order_by('-name', '-date')
    context = {'rooms': rooms}
    return render(request, 'base/index.html', context)


def chatroom(request, slug):
    objects = ChatRoom.objects.get(slug=slug.lower())
    messages = ChatMessages.objects.filter(room=objects)[0:30]
    context = {'chatroom': objects, 'messages': messages}
    return render(request, 'base/room.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        ChatRoom.objects.create(name=name, slug=slug.lower())
        return redirect('rooms')
    return render(request, 'base/create.html')