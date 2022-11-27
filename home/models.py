from datetime import datetime
from django.db import models
from autenticacao.models import CustomUser


class Evento(models.Model):
    titulo = models.CharField(max_length=100,verbose_name='Evento')
    local = models.CharField(max_length=50,verbose_name='Local Do Evento', blank=True,null=True)
    descricao = models.TextField(null=True, blank=True, verbose_name='Descrição Do Evento')
    data_evento  =  models.DateTimeField(verbose_name='Data dos Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação Do Evento')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'evento'
        
    def __str__(self):
        return self.titulo
    
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
    