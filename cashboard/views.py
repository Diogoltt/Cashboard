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
    return redirect('index')


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


@login_required
def financas(request):
    return render(request, 'financas.html')

@login_required
def categoria_view(request, categoria):
    # Filtro por categoria
    despesas = Despesa.objects.filter(user=request.user, categoria=categoria)
    receitas = Receita.objects.filter(user=request.user, categoria=categoria)
    
    context = {
        "categoria": categoria,
        "despesas": despesas,
        "receitas": receitas,
    }
    return render(request, "categoria_view.html", context)


@login_required
def add_financa(request):
    if request.method == 'POST':
        valor = request.POST.get('valor')
        data = request.POST.get('dataFinalMeta')
        descricao = request.POST.get('descricaoMeta')
        categoria = request.POST.get('categoria')
        tipo = request.POST.get('tipo')
        pagamento = request.POST.get('transacao')
        print(valor, data, categoria, tipo)

        if tipo == 'entrada':
            # Cria e salva uma nova receita no banco de dados
            Receita.objects.create(valor=valor, data=data, descricao=descricao, categoria=categoria, user=request.user)
        elif tipo == 'saida':
            # Cria e salva uma nova despesa no banco de dados
            Despesa.objects.create(valor=valor, data=data, descricao=descricao, categoria=categoria, pagamento=pagamento, user=request.user)
        
        return redirect('financas')  # Redireciona para a página de finanças após salvar
