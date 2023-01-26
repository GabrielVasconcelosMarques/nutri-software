from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from .models import Pacientes, DadosPaciente
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt



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
        peso = request.POST.get('peso').replace(',', '.')
        altura = request.POST.get('altura').replace(',', '.')
        biceps = request.POST.get('biceps').replace(',', '.')
        triceps = request.POST.get('triceps').replace(',', '.')
        axilar_media = request.POST.get('axilar_media').replace(',', '.')
        torax = request.POST.get('torax').replace(',', '.')
        abdominal = request.POST.get('abdominal').replace(',', '.')
        suprailiaca = request.POST.get('suprailiaca').replace(',', '.')
        subescapular = request.POST.get('subescapular').replace(',', '.')
        coxa = request.POST.get('coxa').replace(',', '.')
        panturrilha = request.POST.get('panturrilha').replace(',', '.')
        peitoral = request.POST.get('peitoral').replace(',', '.')
        abdomen = request.POST.get('abdomen').replace(',', '.')
        cintura = request.POST.get('cintura').replace(',', '.')
        quadril = request.POST.get('quadril').replace(',', '.')
        pescoco = request.POST.get('pescoco').replace(',', '.')
        coxa_e = request.POST.get('coxa_e').replace(',', '.')
        coxa_d = request.POST.get('coxa_d').replace(',', '.')
        panturrilha_e = request.POST.get('panturrilha_e').replace(',', '.')
        panturrilha_d = request.POST.get('panturrilha_d').replace(',', '.')
        punho_e = request.POST.get('punho_e').replace(',', '.')
        punho_d = request.POST.get('punho_d').replace(',', '.')
        braco_e = request.POST.get('braco_e').replace(',', '.')
        braco_d = request.POST.get('braco_d').replace(',', '.')
        antebraco_e = request.POST.get('antebraco_e').replace(',', '.')
        antebraco_d = request.POST.get('antebraco_d').replace(',', '.')

        
        a = antebraco_e.replace('.', '')
        print(a.replace('.', '').isnumeric())

        if not peso.replace('.', '').isnumeric() or not altura.replace('.', '').isnumeric() or not biceps.replace('.', '').isnumeric() or not triceps.replace('.', '').isnumeric() or not axilar_media.replace('.', '').isnumeric() or not torax.replace('.', '').isnumeric() or not abdominal.replace('.', '').isnumeric() or not suprailiaca.replace('.', '').isnumeric() or not subescapular.replace('.', '').isnumeric() or not coxa.replace('.', '').isnumeric() or not panturrilha.replace('.', '').isnumeric() or not peitoral.replace('.', '').isnumeric() or not abdomen.replace('.', '').isnumeric() or not cintura.replace('.', '').isnumeric() or not quadril.replace('.', '').isnumeric() or not pescoco.replace('.', '').isnumeric() or not coxa_e.replace('.', '').isnumeric() or not coxa_d.replace('.', '').isnumeric() or not panturrilha_e.replace('.', '').isnumeric() or not panturrilha_d.replace('.', '').isnumeric() or not punho_e.replace('.', '').isnumeric() or not punho_d.replace('.', '').isnumeric() or not braco_e.replace('.', '').isnumeric() or not braco_d.replace('.', '').isnumeric() or not antebraco_e.replace('.', '').isnumeric() or not antebraco_d.replace('.', '').isnumeric():
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



@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_peso(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    pesos = [dado.peso for dado in dados]
    labels = list(range(len(pesos)))
    data = {'peso': pesos,
    'labels': labels}
    return JsonResponse(data)

@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_imc(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    imcs = [dado.get_imc() for dado in dados]
    labels = list(range(len(imcs)))
    data = {'imc': imcs,
    'labels': labels}
    return JsonResponse(data)
        
            

        