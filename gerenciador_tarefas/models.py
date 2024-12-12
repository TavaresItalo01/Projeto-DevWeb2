from datetime import date
from django.db import models
from gerenciador_usuario.models import Usuario


class Tarefa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)
    titulo = models.CharField(verbose_name="Titúlo da tarefa",max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(verbose_name="Data da entrega",null=False, blank=False)
    data_finalizacao = models.DateField(null=True, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["data_finalizacao"]

    def marque_como_completo(self):
        if not self.data_finalizacao:
            self.data_finalizacao = date.today()
            self.save()    



