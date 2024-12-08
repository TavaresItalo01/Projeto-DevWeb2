from django.contrib import admin
from django.urls import path

from gerenciador_tarefas.views import lista_tarefas

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lista_tarefas),
]
