from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False)
    matricula = models.CharField(max_length=8, null=False, unique=True)
    email = models.CharField(max_length=255, null=True)