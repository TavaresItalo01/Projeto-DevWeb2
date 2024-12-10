from django.db import models

class Usuario(models.Model) :
    nome = models.CharField(verbose_name="Nome usuario",max_length=100, null=False, blank=False)
    email = models.CharField(verbose_name="email", max_length=100, null=False, blank=False)
    senha = models.CharField(verbose_name="senha", max_length=100, null=False, blank=False)

    

