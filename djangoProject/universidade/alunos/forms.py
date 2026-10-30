from django import forms

from .models import Aluno


class ProdutoForm(forms.ModelForm):
  class Meta:
    model = Aluno
    fields = ['nome', 'preco', 'descricao', 'quantidade_estoque', 'url', 'categoria']
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
      'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
      'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,}),
      'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
      'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
      'categoria': forms.Select(attrs={'class': 'form-control'}),
    }
    labels = {
      'nome': 'Nome do Produto',
      'preco': 'Preço',
      'descricao': 'Descrição',
      'quantidade_estoque': 'Quantidade em Estoque',
      'url': 'URL',
      'categoria': 'Categoria',
    }
