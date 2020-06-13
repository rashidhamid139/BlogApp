from django.urls import path
from .views import RoomList, RoomCreate, RoomUpdate, RoomDelete, RoomDetail
from django.views.generic.base import TemplateView
app_name='rooms'
urlpatterns = [
    path('', TemplateView.as_view(template_name= "rooms/main.html"), name='room-main'),
    path('list/', RoomList.as_view(), name='room-list'),
    path('create/', RoomCreate, name='room-create'),
    path('update/<int:pk>/', RoomUpdate.as_view(), name='room-update'),
    path('delete/<int:pk>/', RoomDelete.as_view(), name='roon-delete'),
    path('<int:pk>/', RoomDetail.as_view(), name='room-detail'),
]