from django.urls import path, include
from . import views

urlpatterns = [
    path('paciente/', views.paciente, name='pacientes'),
    path('paciente/<str:id>/', views.dados_paciente, name="dados_paciente"),
]