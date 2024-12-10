from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from gerenciador_usuario.models import Usuario
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

class UsuarioCreateView(CreateView) :
    model = Usuario
    fields = ["nome", "email", "senha"]
    success_url = reverse_lazy("tarefa_lista")

def login_view(request):
    return render(request, 'gerenciador_usuario/login.html')