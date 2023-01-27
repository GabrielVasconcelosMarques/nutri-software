from django.urls import path, include
from . import views

urlpatterns = [
    path('paciente/', views.paciente, name='pacientes'),
    path('paciente/<str:id>/', views.dados_paciente, name="dados_paciente"),
    path('consultar_paciente/', views.consultar_paciente, name="consultar_paciente"),
    path('grafico_peso/<str:id>/', views.grafico_peso, name="grafico_peso"),
    path('grafico_imc/<str:id>/', views.grafico_imc, name="grafico_peso"),
]