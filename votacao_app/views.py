from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Aluno, Grupo, Votacao
from django.contrib.auth import authenticate, login
from django.http import HttpResponseNotFound
import random

def home(request):
    if request.method == 'POST':
        cookies = request.COOKIES
        reponse = render(request, 'verificar_senha.html')
        email = request.POST.get('email')
        reponse.set_cookie('email', email)
        try:
            aluno = Aluno.objects.get(email=email)
            num = random.randint(1000, 9999)
            num = str(num)
            aluno.codigo = num
            aluno.save()
            send_mail('assunto', num, 'votacaoproz@gmail.com', [email, ])
            print(num)
            reponse = render(request, 'verificar_senha.html')
            reponse.set_cookie('email', email)
            return reponse
        except Aluno.DoesNotExist:
            aluno = None
            reponse = render(request, 'login.html', {'messages': 'email-nao-cadastrado'})

            return reponse
    else:
        reponse = render(request, 'login.html', {'messages': None})
        return reponse

def verificar(request):
    cookies = request.COOKIES
    email = cookies['email']
    emails = Aluno.objects.values_list('email')
    x = []
    for mail in emails:
        x.append(mail[0])
    if email in x:
        cod = Aluno.objects.get(email=email)
        cod1 = request.POST.get('cod1', 'None')
        cod2 = request.POST.get('cod2', 'None')
        cod3 = request.POST.get('cod3', 'None')
        cod4 = request.POST.get('cod4', 'None')
        cods = cod1 + cod2 + cod3 + cod4
        print(cod.nome)
        if cod.codigo == cods:
            try:
                user = User.objects.get(username=cod.nome)
                # user.set_password(cod.codigo)
                user.save
                login(request, user)
                print(user.is_authenticated)
                return redirect('votacao')
            except:
                print(465)
                user = User.objects.create_user(
                    cod.nome, cod.email, cod.codigo)
                login(request, user)
            return redirect(request, votacao)
        else:
            return render(request, 'verificar_senha.html')
    else:
        reponse = render(request, 'login.html', {'msg': 'teste'})
        reponse.set_cookie('email', cookies['email'])
        return reponse


def votacao(request):
    # try:
    user = request.user
    grupos = Grupo.objects.values_list('nome_grupo')
    aluno = Aluno.objects.get(nome=user.username)
    grupos_tratados = []
    for i in grupos:
        grupos_tratados.append(i[0])
    voto = request.POST.get('grupo')
    grupos_tratados.remove(aluno.grupo.nome_grupo)
    print(voto, Votacao.objects.filter(aluno=user.username).exists())
    if user.is_authenticated:
        if voto:
            if not Votacao.objects.filter(aluno=user.username).exists():
                votacao = Votacao.objects.create(
                    aluno=user.username, grupo=voto)
                voto = False
            else:
                return render(request, 'confirmar-voto.html', {'user': user})
        if Votacao.objects.filter(aluno=user.username).exists():
            return render(request, 'confirmar-voto.html', {'user': user})
        return render(request, 'tela_votacao.html', {'grupos': grupos_tratados})
    else:
        return redirect(verificar, {'messages': 'teste'})
    # except:
    #     return HttpResponseNotFound('ola')
