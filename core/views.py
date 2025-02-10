from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

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
