from django.urls import path
from .views import dynamic

urlpatterns = [
    path('', dynamic, name='nondynamic'),
]