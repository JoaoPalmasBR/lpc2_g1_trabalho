from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    sexos = (
        (u'FEM',u'FEM'),
        (u'MAS',u'MAS'),
    )
    sexo = models.CharField(max_length=7, choices=sexos)
    cpf = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    usuario = models.ForeignKey(User, null=True, blank=False)
class Evento(models.Model):
    nome = models.CharField(max_length=128)
    dataInicio = models.DateTimeField(blank=True, null=True)
    dataFim = models.DateTimeField(blank=True, null=True)
    realizador = models.ForeignKey(Pessoa, null=True, blank=False)
class Ticket(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.CharField(max_length=256)
    valor = models.CharField(max_length=128)
    evento = models.ForeignKey(Evento, null=True, blank=False)
class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, null=True, blank=False)
    pessoa = models.ForeignKey(Pessoa, null=True, blank=False)
    ticket = models.ForeignKey(Ticket, null=True, blank=False)
    validacao = models.BooleanField(default=True)