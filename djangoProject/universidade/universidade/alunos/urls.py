from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('listar_alunos', views.listar_alunos, name='listar_alunos'),
    path('detalhar_aluno/<int:id>', views.detalhar_aluno, name='detalhar_aluno')
]