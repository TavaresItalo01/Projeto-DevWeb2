from .models import Tarefa
from .forms import TarefaForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class TarefasListView(LoginRequiredMixin, ListView):
    model = Tarefa
    template_name = 'gerenciador_tarefas/tarefa_list.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)


class TarefaCreateView(LoginRequiredMixin, CreateView) :
    model = Tarefa
    form_class = TarefaForm
    template_name = "gerenciador_tarefas/tarefa_form.html"
    success_url = reverse_lazy("tarefa_lista")

    def form_valid(self, form):
        form.instance.user = self.request.user
   
    

class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'gerenciador_tarefas/tarefa_form.html'
    success_url = reverse_lazy('lista_tarefas')

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user) 

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'tarefas/tarefa_confirm_delete.html'
    success_url = reverse_lazy('lista_tarefas')

    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user) 

class TarefaCompleteView(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
        tarefa.marque_como_completo()
        return redirect("tarefa_lista")   
