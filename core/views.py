from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegistrationForm
from django.views.generic.edit import UpdateView

def registrar(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('home')  # Redireciona para a página de tarefas
    else:
        form = UserRegistrationForm()

    return render(request, 'usuarios/registro.html', {'form': form})

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'usuarios/editar_perfil.html'  
    fields = ['username','first_name','email']  # Campos que o usuário pode editar

    success_url = reverse_lazy('home')  # Para onde redirecionar após a edição

    def get_object(self):
        return self.request.user 
