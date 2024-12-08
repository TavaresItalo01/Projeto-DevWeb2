from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "gerenciador_tarefas/lista_tarefas.html", {"tarefas": tarefas}) 
