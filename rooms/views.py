from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, CreateView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .forms import RoomForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import Room
from django.template.loader import render_to_string
import json

class RoomList(View):
    def get(self, request):
        rooms = list(Room.objects.all().values())
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
        print(request.POST)
        form = RoomForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.is_valid())
            form.save()
            form = RoomForm()
            data['message'] = "Form Submitted"
        else:
            data['error'] = 'form not valid'
        # return HttpResponseRedirect(reverse('rooms:room-list'))
        return JsonResponse(data)
    else:
        form = RoomForm()
        html = render_to_string('rooms/roomscreate.html', {'form': form})
        return HttpResponse(html)



# @method_decorator(csrf_exempt, name='dispatch')
# class RoomCreate(CreateView):
#     def post(self, request):
#         data = dict()
#         form = RoomForm(request.POST)
#         if form.is_valid():
#             room = form.save()
#             data['room'] = model_to_dict(room)
#         else:
#             data['error'] = 'form not valid!'
#         return JsonResponse(data)
#     def get(self, request):


class RoomUpdate(View):
    def post(self, request, pk):
        data = dict()
        room = Room.objects.get(pk=pk)
        form = RoomForm(instance=room, data= request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] = 'form not valid'
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class RoomDelete(View):
    def post(self, request, pk):
        data = dict()
        room = Room.objects.get(pk=pk)
        print(room)
        if room:
            room.delete()
            data['message'] = "Room Deleted"
        else:
            data['error'] = "Error!"
        return JsonResponse(data)

