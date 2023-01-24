from django.urls import path, include
from . import views

urlpatterns = [
    path('pacientes/', views.paciente, name='pacientes')
]