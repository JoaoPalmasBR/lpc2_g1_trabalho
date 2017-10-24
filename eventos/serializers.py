from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eventos.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email', 'is_staff')

class PessoaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Pessoa
        fields = ('url','nome','sexo','cpf', 'cidade', 'estado', 'usuario')

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('url','nome', 'dataInicio', 'dataFim', 'realizador')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('url','nome', 'descricao', 'valor', 'evento')

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ('url','evento', 'pessoa', 'ticket', 'validacao')