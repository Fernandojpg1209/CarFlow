from django.contrib import admin
from .models import Produto, Servico, Agendamento

admin.site.register(Produto)
admin.site.register(Servico)
admin.site.register(Agendamento)