from django.contrib import admin
from core.models import Evento
# Register your models here.

class EvetnoAdmin(admin.ModelAdmin):
    list_display = ('titulo','id', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, EvetnoAdmin)

