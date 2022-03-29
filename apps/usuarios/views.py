from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
from receita.models import receita_modelo
def loguin(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == '' or senha == '':
            print('valores em branco')
            return redirect('loguin')
        #a linha abaixo verifica se o email existe no banco de dados dentro de User
        if User.objects.filter(email=email).exists():
            # pega o valor dentro do email filtra vai nos valores e busca username
            # ou seja pega o valor dentro do email e pega o nome
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            #pega e autentica os valores
            user = auth.authenticate(request, username=nome , password=senha)
            if user is not None:
                auth.login(request,user)
                print('login realizado')
                return redirect('dashbord')
    return render(request, 'usuarios/loguin.html')
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('nome do usuario em branco')
            return redirect('cadastro')
        if not email.strip():
            print('email em branco')
            return redirect('cadastro')
        if password != password2:
            messages.error(request,'senhas diferentes')
            print('senhas diferentes')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('usuario ja cadastrado')
        usuario = User.objects.create_user(username=nome,email=email,password=password)
        usuario.save()
        messages.success(request,'usuario cadastrado')
        print('usuario cadastrado com suceso')
        return redirect('loguin')
    else:
        return render(request,'usuarios/cadastro.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashbord(request):
    if request.user.is_authenticated:
        id = request.user.id
        receita = receita_modelo.objects.order_by('-data_receita').filter(pessoa=id)
        dados = {
            'receitas': receita
        }
        return render(request, 'usuarios/dashbord.html',dados)
    else:
        return redirect('index')

