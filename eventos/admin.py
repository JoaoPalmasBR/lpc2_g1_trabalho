from django.contrib import admin
from eventos.models import *

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Evento)
admin.site.register(Ticket)
admin.site.register(Inscricao)