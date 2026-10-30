from django.shortcuts import render
from .models import Aluno

# Create your views here.
def index(request):
        return render(request, 'alunos/index.html', {})

def sobre(request):
        return render(request, 'alunos/sobre.html', {'nome_projeto': 'Universidade'})

def listar_alunos(request):
        alunos = Aluno.objects.all()
        return render(request, 'alunos/listar_alunos.html', {'alunos': alunos})