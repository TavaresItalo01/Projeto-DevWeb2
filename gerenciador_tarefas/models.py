from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError


class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(verbose_name="Titúlo da tarefa",max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateField(verbose_name="Data da entrega",null=False, blank=False)
    data_finalizacao = models.DateField(null=True, blank=False)
    descricao = models.TextField(default="Descrição não fornecida")
    email = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["data_finalizacao"]

    def marque_como_completo(self):
        if not self.data_finalizacao:
            self.data_finalizacao = date.today()
            self.save()  

    def clean(self):
        if not self.data_entrega:
            raise ValidationError("A data de entrega não pode ser vazia.")
        
        # Comparar a data de entrega com a data de hoje
        if self.data_entrega < date.today():
            raise ValidationError("A data de entrega não pode ser anterior à data de hoje.")

    def save(self, *args, **kwargs):
        # Chama o método clean antes de salvar o modelo
        self.clean()
        super(Tarefa, self).save(*args, **kwargs) 


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarefa = models.ForeignKey('Tarefa', on_delete=models.CASCADE, related_name='comentarios')
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.usuario.username} em {self.tarefa.titulo}"
