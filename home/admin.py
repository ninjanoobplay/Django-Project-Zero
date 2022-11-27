from django.contrib import admin

from home.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','usuario', 'data_evento','descricao', 'data_criacao')
    list_filter = ('usuario',)

admin.site.register(Evento, EventoAdmin)
