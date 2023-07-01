from django.shortcuts import render, HttpResponse ,redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Aluno,Grupo
from django.contrib.auth import authenticate, login
import random


def home(request):
    cookies = request.COOKIES
    email = request.POST.get('email')
    reponse = render(request, 'verificar_senha.html')
    reponse.set_cookie('email', email)
    emails = Aluno.objects.values_list('email')
    x = []
    for mail in emails:
        x.append(mail[0])
    msg = x
    if email in x:
        num = random.randint(1000, 9999)
        num = str(num)
        cod = Aluno.objects.get(email=email)
        cod.codigo = num
        cod.save()
        send_mail('assunto', num, 'votacaoproz@gmail.com', [email, ])
        reponse = render(request, 'verificar_senha.html')
        reponse.set_cookie('email', email)
        return reponse

    elif email == None:
        reponse = render(request, 'login.html', {'messages': None})
        reponse.set_cookie('email', email)
        return reponse
    else:
        reponse = render(request, 'login.html', {'messages': 'teste'})
        reponse.set_cookie('email', email)
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
                login(request,user)
                print(user.is_authenticated) 
                return redirect('votacao')            
            except:                
                print(465)
                user = User.objects.create_user(cod.nome,cod.email,cod.codigo)
                login(request,user) 
            return redirect(request,votacao)
        else:
            return render(request, 'verificar_senha.html')
    else:
        reponse = render(request, 'login.html', {'msg': 'teste'})
        reponse.set_cookie('email', cookies['email'])
        return reponse
    

def votacao(request):
    user = request.user
    grupos = Grupo.objects.values_list('nome_grupo')
    aluno = Aluno.objects.get(nome = user.username)
    grupos_tratados = []
    for i in grupos:
        grupos_tratados.append(i[0])
    voto = request.POST.get('grupo')
    grupos_tratados.remove('teste')
    grupos_tratados.remove(aluno.grupo.nome_grupo)
    print(grupos_tratados,grupos,aluno.grupo.nome_grupo)
    if user.is_authenticated:
        
        return render(request, 'tela_votacao.html',{'grupos':grupos_tratados})
    else:
        return redirect(verificar,{'messages': 'teste'})
        
    