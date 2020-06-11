from django.urls import path
from .views import dynamic

urlpatterns = [
    path('nondynamic/', dynamic, name='nondynamic'),
]