from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('listar_alunos', views.listar_alunos, name='listar_alunos'),
    
]