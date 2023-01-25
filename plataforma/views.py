from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import Pacientes, DadosPaciente
from datetime import datetime



@login_required(login_url='/auth/login/')
def paciente(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'pacientes.html', {'pacientes' : pacientes})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        usuario = request.user.id

        if (len(nome.strip()) == 0) or (len(sexo.strip()) == 0) or (len(idade.strip()) == 0) or (len(email.strip()) == 0) or (len(telefone.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/paciente/')
        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite uma idade válida')
            return redirect('/paciente/')

        pacientes = Pacientes.objects.filter(email=email, nutri=usuario)

        if pacientes.exists():
            messages.add_message(request, constants.ERROR, f'Já existe um paciente com o e-mail {email} para o nutricionista {request.user.username}')
            return redirect('/paciente/')
        
        try:
            paciente = Pacientes(nome=nome,
                                sexo=sexo,
                                idade=idade,
                                email=email,
                                telefone=telefone,
                                nutri=request.user
            )

            paciente.save()
            messages.add_message(request, constants.SUCCESS, 'Paciente cadastrado com sucesso')
            return redirect('/paciente/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/paciente/')


@login_required(login_url='/auth/login/')
def dados_paciente(request, id):
    if request.method == 'GET':
        paciente = get_object_or_404(Pacientes, id=id, nutri=request.user)
        dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
        return render(request, 'dados_paciente.html', {'paciente' : paciente, 'dados_paciente' : dados_paciente})
    elif request.method == "POST":
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        biceps = request.POST.get('biceps')
        triceps = request.POST.get('triceps')
        axilar_media = request.POST.get('axilar_media')
        torax = request.POST.get('torax')
        abdominal = request.POST.get('abdominal')
        suprailiaca = request.POST.get('suprailiaca')
        subescapular = request.POST.get('subescapular')
        coxa = request.POST.get('coxa')
        panturrilha = request.POST.get('panturrilha')
        peitoral = request.POST.get('peitoral')
        abdomen = request.POST.get('abdomen')
        cintura = request.POST.get('cintura')
        quadril = request.POST.get('quadril')
        pescoco = request.POST.get('pescoco')
        coxa_e = request.POST.get('coxa_e')
        coxa_d = request.POST.get('coxa_d')
        panturrilha_e = request.POST.get('panturrilha_e')
        panturrilha_d = request.POST.get('panturrilha_d')
        punho_e = request.POST.get('punho_e')
        punho_d = request.POST.get('punho_d')
        braco_e = request.POST.get('braco_e')
        braco_d = request.POST.get('braco_d')
        antebraco_e = request.POST.get('antebraco_e')
        antebraco_d = request.POST.get('antebraco_d')

        if not peso.isnumeric() or not altura.isnumeric() or not biceps.isnumeric() or not triceps.isnumeric() or not axilar_media.isnumeric() or not torax.isnumeric() or not abdominal.isnumeric() or not suprailiaca.isnumeric() or not subescapular.isnumeric() or not coxa.isnumeric() or not panturrilha.isnumeric() or not peitoral.isnumeric() or not abdomen.isnumeric() or not cintura.isnumeric() or not quadril.isnumeric() or not pescoco.isnumeric() or not coxa_e.isnumeric() or not coxa_d.isnumeric() or not panturrilha_e.isnumeric() or not panturrilha_d.isnumeric() or not punho_e.isnumeric() or not punho_d.isnumeric() or not braco_e.isnumeric() or not braco_d.isnumeric() or not antebraco_e.isnumeric() or not antebraco_d.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite um valor numérico para os campos de medidas')
            return redirect('/paciente/')

        try:
            paciente = get_object_or_404(Pacientes, id=id, nutri=request.user)
            dados_paciente = DadosPaciente(paciente=paciente,
                                    data=datetime.now(),
                                    peso=peso,
                                    altura=altura,
                                    biceps=biceps,
                                    triceps=triceps,
                                    axilar_media=axilar_media,
                                    torax=torax,
                                    abdominal=abdominal,
                                    suprailiaca=suprailiaca,
                                    subescapular=subescapular,
                                    coxa=coxa,
                                    panturrilha=panturrilha,
                                    peitoral=peitoral,
                                    abdomen=abdomen,
                                    cintura=cintura,
                                    quadril=quadril,
                                    pescoco=pescoco,
                                    coxa_e=coxa_e,
                                    coxa_d=coxa_d,
                                    panturrilha_e=panturrilha_e,
                                    panturrilha_d=panturrilha_d,
                                    punho_e=punho_e,
                                    punho_d=punho_d,
                                    braco_e=braco_e,
                                    braco_d=braco_d,
                                    antebraco_e=antebraco_e,
                                    antebraco_d=antebraco_d)

            dados_paciente.save()
            messages.add_message(request, constants.SUCCESS, 'Dados cadastrados com sucesso')
            return redirect('/paciente/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/paciente/')
        
            

        