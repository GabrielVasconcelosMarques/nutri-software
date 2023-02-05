from django.urls import path, include
from . import views

urlpatterns = [
    path('paciente/', views.paciente, name='pacientes'),
    path('paciente/<str:id>/', views.dados_paciente, name="dados_paciente"),
    path('consultar_paciente/', views.consultar_paciente, name="consultar_paciente"),
    path('grafico_peso/<str:id>/', views.grafico_peso, name="grafico_peso"),
    path('grafico_imc/<str:id>/', views.grafico_imc, name="grafico_imc"),
    path('plano_alimentar_listar/', views.plano_alimentar_listar, name="plano_alimentar_listar"),
    path('plano_alimentar/<str:id>', views.plano_alimentar, name="plano_alimentar"),
    path('refeicao/<str:id>/', views.refeicao, name="refeicao"),
]