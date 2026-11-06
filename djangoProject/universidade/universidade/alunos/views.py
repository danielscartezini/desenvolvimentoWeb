from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def index(request):
        return render(request, 'alunos/index.html', {})

def sobre(request):
        return render(request, 'alunos/sobre.html', {'nome_projeto': 'Universidade'})

def listar_alunos(request):
        alunos = Aluno.objects.all()
        return render(request, 'alunos/listar_alunos.html', {'alunos': alunos})

def detalhar_aluno(request, id):
        aluno = None
        try:
                aluno = Aluno.objects.get(pk=id)
        except:
                pass
        return render(request, 'alunos/detalhar_aluno.html', {'aluno': aluno})

def cadastrar_aluno(request):
        if request.POST:
                form = AlunoForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, "Aluno cadastrado com sucesso.")
                        return redirect('listar_alunos')
                messages.error(request, "Erro no preenchimento do formulário.")
                return render(request, 'alunos/form_aluno.html', {'form': form})
        form = AlunoForm()
        return render(request, 'alunos/form_aluno.html', {'form': form})

def alterar_aluno(request, id):
        aluno = Aluno.objects.get(pk=id)
        if request.POST:
                form = AlunoForm(request.POST, instance=aluno)
                if form.is_valid():
                        form.save()
                        messages.success(request, "Aluno alterado com sucesso.")
                        return redirect('listar_alunos')
                messages.error(request, "Erro no preenchimento do formulário.")
                return render(request, 'alunos/form_aluno.html', {'form': form, 'editar': True})
        form = AlunoForm(instance=aluno)
        return render(request, 'alunos/form_aluno.html', {'form': form, 'editar': True})

def excluir_aluno(request, id):
        aluno = Aluno.objects.get(pk=id)
        if request.POST:
                aluno.delete()
                messages.success(request, "Aluno deletado com sucesso.")
                return redirect('listar_alunos')
        return render(request, 'alunos/excluir_aluno.html', {'aluno': aluno})