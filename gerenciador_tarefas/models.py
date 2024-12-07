from django.db import models
from models import Usuario


class Tarefa(models.Model):
    usuario = Usuario.nome
    titulo = models.CharField(max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateTimeField(null=False, blank=False)
    data_finalizacao = models.DateTimeField(null=True)

class Usuario(models.Model) :
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField(null=False, blank=False)
