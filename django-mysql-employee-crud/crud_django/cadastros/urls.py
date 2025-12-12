# cadastros/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pessoas, name='listar_pessoas'),
    path('criar/', views.criar_pessoa, name='criar_pessoa'),
    path('atualizar/<int:pk>/', views.atualizar_pessoa, name='atualizar_pessoa'),
    path('deletar/<int:pk>/', views.deletar_pessoa, name='deletar_pessoa'),
]