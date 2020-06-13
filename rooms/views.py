from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, CreateView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import RoomForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Room
from django.core import serializers
from django.template.loader import render_to_string
import json

class RoomList(View):
    def get(self, request):
        rooms = list(Room.objects.all().values().order_by('-pk'))
        data = dict()
        data['rooms'] = rooms
        return JsonResponse(data)
    


class RoomDetail(View):
    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        data = dict()
        data['room'] = model_to_dict(room)
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
def RoomCreate(request):
    if request.method == 'POST':
        data = dict()
        form = RoomForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({'instance': ser_instance}, status= 200)
        else:  
            return JsonResponse({'error': form.errors}, statuc=400)
        
    else:
        form = RoomForm()
        html = render_to_string('rooms/roomscreate.html', {'form': form})
        return HttpResponse(html)


@method_decorator(csrf_exempt, name='dispatch')
class RoomUpdate(View):
    def get(self, request, pk):
        room = Room.objects.get(pk=pk)
        data = { 'name': room.name, 'room_number': room.room_number, 'status': room.status, 'room_type': room.room_type, 'nobeds': room.nobeds}

        form =  RoomForm(instance=room, initial=data)
        html = render_to_string('rooms/roomupdate.html', {'form':form, 'room_id':pk})
        return HttpResponse(html)

    def post(self, request, pk):
        data = dict()
        room = Room.objects.get(pk=pk)
        form = RoomForm(instance=room, data= request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize('json', [instance, ])
            return JsonResponse({'instance':ser_instance}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
            
@method_decorator(csrf_exempt, name='dispatch')
class RoomDelete(View):
    def post(self, request, pk):
        data = dict()
        room = Room.objects.get(pk=pk)
        if room:
            room.delete()
            data['message'] = "Room Deleted"
        else:
            data['error'] = "Error!"
        return JsonResponse(data)

