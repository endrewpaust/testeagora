from django.shortcuts import render,get_object_or_404,get_list_or_404,redirect
from receita.models import receita_modelo
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def index(request):
    recei = receita_modelo.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(recei, 1)
    page = request.GET.get('page')
    receitas_por_paginas = paginator.get_page(page)
    dados = {
        'receitas' : receitas_por_paginas
    }
    return render(request,'receita/index.html',dados)
def receita(request,receita_id):
    receita = get_object_or_404(receita_modelo, pk=receita_id)
    receita_exibir = {
        'receita': receita
    }
    return render(request,'receita/receita.html',receita_exibir)
def buscar(request):
    lista_receitas = receita_modelo.objects.order_by('-data_receita').filter(publicada=True)
    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_buscar)
    dados = {
        'receitas': lista_receitas,
    }

    return render(request, 'receita/buscar.html',dados)
def cria_receita(request):
    if request.method == 'POST':
        nome_da_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_de_preparo = request.POST['modo_de_preparo']
        tempo_de_preparo = request.POST['tempo_de_preparo']
        rendimemto = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = receita_modelo.objects.create(pessoa=user,
        nome_receita=nome_da_receita,ingredientes=ingredientes,
        modo_de_preparo=modo_de_preparo,tempo_de_preparo=tempo_de_preparo,
        rendimento=rendimemto,categoria=categoria,foto_receita=foto)
        receita.save()
        return redirect('dashbord')
    else:
        return render(request, 'receita/cria_receita.html')
def deleta_receita(request,receita_id):
    receita = get_object_or_404(receita_modelo, pk=receita_id)
    receita.delete()
    return redirect('dashbord')
def edita_receita(request,receita_id):
    receita = get_object_or_404(receita_modelo, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request,'receita/edita_receita.html',receita_a_editar)
def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = receita_modelo.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_de_preparo = request.POST['modo_de_preparo']
        r.tempo_de_preparo = request.POST['tempo_de_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']
        r.save()
        return redirect('dashbord')

