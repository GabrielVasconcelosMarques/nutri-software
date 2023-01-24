from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages, auth


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        # usando auth do django para autenticar com user e senha
        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/auth/login')