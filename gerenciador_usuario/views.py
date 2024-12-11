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

#email
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse

def enviar_email(request):

    if request.POST:
        nome = request.POST.get('nome')
        mensagem = request.POST.get('msg')
        destinatario = request.POST.get('email')

        email = EmailMessage(subject=nome, body=mensagem,
                             from_email=settings.EMAIL_HOST_USER,
                             to=[destinatario])
        email.send()

        return HttpResponse('E-mail enviado com sucesso!')

    return render(request, 'index.html',)