from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastrar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home/')
        return render(request, 'cadastrar.html')
    elif request.method == "POST":
        username = request.POST.get('username').lower().strip()
        email = request.POST.get('email').lower().strip()
        primeiro_nome = request.POST.get('first_name').lower().strip()
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastrar')

        if len(username.strip()) == 0 or len(senha.strip()) == 0 or len(email.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastrar')
        
        user = CustomUser.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse nome')
            return redirect('/auth/cadastrar')
        
        user_email = CustomUser.objects.filter(email=email)

        if user_email.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse Email')
            return redirect('/auth/cadastrar')

        try:
            user = CustomUser.objects.create_user(username=username,
                                    password=senha,email=email,first_name=primeiro_nome)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Conta Criada Com Sucesso!')
            return redirect('/auth/logar')
        except:
            return redirect('/auth/cadastrar')

def logar(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect('/home/')
        return render(request, 'logar.html')
    elif request.method=="POST":
        usern = request.POST.get('username')
        username = usern.strip().lower()
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou Senha Inválidos!')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/home/')
    return render(request, 'logar.html')

def sair(request):
    auth.logout(request)
    return redirect ('/auth/logar')