from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa

def lista_tarefas(request):
    nome_usuario = # buscar nome do usuario logado,
    Tarefas = Tarefa.objects.filter()
    return render(request, "gerenciador_tarefas/lista_tarefas.html")

