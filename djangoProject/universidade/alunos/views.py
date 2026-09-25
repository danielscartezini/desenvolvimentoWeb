from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'alunos/index.html', {})

def sobre(request):
    return render(request, alunos/sobre.html, {})
