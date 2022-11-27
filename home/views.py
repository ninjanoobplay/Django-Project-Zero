from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.models import Evento
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime , timedelta

# Create your views here.
def home(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('/auth/logar/')
        return render(request, 'home.html')

def index(request):
    if request.method == "GET":
        return redirect('/home/')
@login_required(login_url='/login/')
def agendamento(request):
    if request.POST:
        titulo = request.POST.get('evento')
        local  = request.POST.get('local_evento')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo, local=local,  data_evento=data_evento,descricao=descricao, usuario=usuario)
        messages.add_message(request, constants.SUCCESS, 'Agendamento Criado Com Sucesso!')
        return redirect('/home/agendamento/')
    
    return render(request, "agendamento.html")


@login_required(login_url='/login/')
def agenda(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=2)
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual)
    dados  = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def submit_delete (request):
    if request.POST:
        try:
            usuario = request.user
            id_evento = request.POST.get('id_evento')
            evento = Evento.objects.get(id=id_evento)
        except Evento.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'Esse ID Não Existe No Seu Usuário!')
            return redirect('/home/agenda/')
        if usuario == evento.usuario:
            evento.delete()
            messages.add_message(request, constants.SUCCESS, 'Agendamento Excluido Com Sucesso!')
        return redirect('/home/agenda/')