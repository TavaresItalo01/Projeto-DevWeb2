from .models import Tarefa
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

class TarefasListView(ListView):
    model = Tarefa


class TarefaCreateView(CreateView) :
    model = Tarefa
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("tarefa_lista")

class TarefaUpdateView(UpdateView):
    model = Tarefa
    fields = ["titulo", "data_entrega"]
    success_url = reverse_lazy("tarefa_lista")

class TarefaDeleteView(DeleteView):
    model = Tarefa
    success_url = reverse_lazy("tarefa_lista")

class TarefaCompleteView(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.marque_como_completo()
        return redirect("tarefa_lista")   
