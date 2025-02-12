from .models import Tarefa
from .forms import TarefaForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Tarefa
from django.core.mail import send_mail
from django.conf import settings


class TarefasListView(LoginRequiredMixin, ListView):
    model = Tarefa
    template_name = 'gerenciador_tarefas/tarefa_list.html'
    context_object_name = 'tarefas'

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)


class TarefaCreateView(LoginRequiredMixin, CreateView) :
    model = Tarefa
    form_class = TarefaForm
    template_name = "gerenciador_tarefas/tarefa_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form) 
   
    

class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'gerenciador_tarefas/tarefa_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user) 

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'gerenciador_tarefas/tarefa_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user) 

class TarefaCompleteView(View):
    def get(self, request, pk):
        tarefa = get_object_or_404(Tarefa, pk=pk)
         # Verifica se o usuário é o dono da tarefa
        if tarefa.usuario != request.user:
            return HttpResponseForbidden("Você não tem permissão para completar esta tarefa.")
        
        # Marca a tarefa como completa
        tarefa.marque_como_completo()

        # Envia o e-mail de notificação
        send_mail(
            subject='Tarefa Completa!',
            message=f'A tarefa "{tarefa.titulo}" foi marcada como completa.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.username],
            fail_silently=False,
        )

        # Feedback para o usuário
        messages.success(request, "Tarefa marcada como completa e e-mail enviado!")

        # Redireciona para a home
        return redirect('home')
