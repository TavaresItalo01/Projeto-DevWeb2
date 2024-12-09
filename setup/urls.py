from django.contrib import admin
from django.urls import path

from gerenciador_tarefas.views import TarefasListView, TarefaCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TarefasListView.as_view(), name="tarefa_lista"),
    path("create", TarefaCreateView.as_view(), name="tarefa_form")
]
