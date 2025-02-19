from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Despesa, Receita
from django.db.models import Sum
from django.contrib import messages
import json
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
MESES = {
    '1': 'Janeiro',
    '2': 'Fevereiro',
    '3': 'Março',
    '4': 'Abril',
    '5': 'Maio',
    '6': 'Junho',
    '7': 'Julho',
    '8': 'Agosto',
    '9': 'Setembro',
    '10': 'Outubro',
    '11': 'Novembro',
    '12': 'Dezembro'
}


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return render(request, 'login.html', {'error': 'Preencha todos os campos'})
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        # Autenticação do usuário
        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('dashboards')  # Redireciona para o dashboard ou página inicial
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'login.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(username, email, password, confirm_password)

        if User.objects.filter(username=username).exists():
            return render(request, 'cadastro.html', {'error': 'Usuário já existe'})

        if User.objects.filter(email=email).exists():
            return render(request, 'cadastro.html', {'error': 'E-mail já cadastrado'})

        # Criação do usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('dashboards')

    return render(request, 'cadastro.html')


def user_logout(request):
    logout(request)
    return redirect('')

@login_required
def mercado(request):
    return render(request, 'mercado.html')

@login_required
def pet(request):
    return render(request, 'pet.html')

@login_required
def lazer(request):
    return render(request, 'lazer.html')

@login_required
def farmacia(request):
    return render(request, 'farmacia.html')

@login_required
def viagem(request):
    return render(request, 'viagem.html')

@login_required
def poupanca(request):
    return render(request, 'poupanca.html')

@login_required
def dashboards(request):
    total_receitas = Receita.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0
    total_despesas = Despesa.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_receitas - total_despesas

    # Consultando as despesas por categoria e pagamento
    despesas_por_categoria = Despesa.objects.values('categoria').annotate(total=Sum('valor'))
    despesas_por_pagamento = Despesa.objects.values('pagamento').annotate(total=Sum('valor'))

    # Convertendo os QuerySets para listas de dicionários
    despesas_por_categoria_list = list(despesas_por_categoria)
    despesas_por_pagamento_list = list(despesas_por_pagamento)

    # Passando os dados para o template como variáveis
    context = {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'despesas_por_categoria': despesas_por_categoria_list,  # Passando dados como JSON
        'despesas_por_pagamento': despesas_por_pagamento_list,  # Passando dados como JSON
    }
    return render(request, 'dashboards.html', context)

def salvar_receita(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')

        # Cria e salva uma nova receita no banco de dados
        Receita.objects.create(valor=valor, data=data, descricao=categoria)

        return redirect('dashboards')  # Redireciona de volta para a página inicial

def salvar_despesa(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        data = request.POST.get('data')
        categoria = request.POST.get('categoria')

        # Cria e salva uma nova despesa no banco de dados
        Despesa.objects.create(valor=valor, data=data, descricao=categoria)

        return redirect('dashboards')  # Redireciona de volta para a página inicial