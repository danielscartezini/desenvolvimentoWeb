from django import forms

from .models import Aluno


class AlunoForm(forms.ModelForm):
  class Meta:
    model = Aluno
    fields = ['nome', 'email', 'matricula']
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do aluno'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'matricula': forms.TextInput(attrs={'class': 'form-control'}),
      }
    labels = {
      'nome': 'Nome do Aluno',
      'email': 'E-mail',
      'matricula': 'Matrícula',
    }
