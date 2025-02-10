from django.urls import path

from gerenciador_tarefas.views import (
    TarefasListView, 
    TarefaCreateView, 
    TarefaUpdateView, 
    TarefaDeleteView,
    TarefaCompleteView,
    )


urlpatterns = [
    path("home", TarefasListView.as_view(), name="tarefa_lista"),
    path("create", TarefaCreateView.as_view(), name="tarefa_form"),
    path("update/<int:pk>", TarefaUpdateView.as_view(), name="tarefa_uptade"),
    path("delete/<int:pk>", TarefaDeleteView.as_view(), name="tarefa_delete"),
    path("complete/<int:pk>",TarefaCompleteView.as_view(), name="tarefa_complete"),
]