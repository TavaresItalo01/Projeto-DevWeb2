from django.contrib import admin
from django.urls import path
from gerenciador_usuario.views import login_view, enviar_email

from gerenciador_tarefas.views import (
    TarefasListView, 
    TarefaCreateView, 
    TarefaUpdateView, 
    TarefaDeleteView,
    TarefaCompleteView,
    )

from gerenciador_usuario.views import UsuarioCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", login_view),
    path("home", TarefasListView.as_view(), name="tarefa_lista"),
    path("create", TarefaCreateView.as_view(), name="tarefa_form"),
    path("update/<int:pk>", TarefaUpdateView.as_view(), name="tarefa_uptade"),
    path("delete/<int:pk>", TarefaDeleteView.as_view(), name="tarefa_delete"),
    path("complete/<int:pk>",TarefaCompleteView.as_view(), name="tarefa_complete"),
    path("createuser", UsuarioCreateView.as_view(), name="usuario_form" ),
    path('email', enviar_email, name='enviar_email'),
]
