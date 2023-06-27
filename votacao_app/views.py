from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Validacao ,EmailConfirmacao
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
import random

# @login_required
def home(request):
    cookies = request.COOKIES
    email = request.POST.get('email')
    reponse = render(request, 'verificar_senha.html')
    reponse.set_cookie('email',email)
    print(cookies['email'])
    emails = EmailConfirmacao.objects.values_list('emails')
    x=[]
    for mail in emails:
        x.append(mail[0])
    msg = x
    if email in x:
        num = random.randint(1000, 9999)
        num = str(num)
        cod = Validacao.objects.get(email=email)
        cod.codido = num  
        cod.save()   
        print(cod.email,cod.codido)          
        send_mail('assunto',num,'votacaoproz@gmail.com',[email,])
        
        reponse = render(request, 'verificar_senha.html')
        reponse.set_cookie('email',email)
        return reponse  
        
    else:
        print('aqui',email)
        reponse = render(request, 'login.html', {'msg': 'teste'})
        reponse.set_cookie('email',email)
        return reponse  


def verificar(request):
    cookies = request.COOKIES
    email =cookies['email']
    emails = EmailConfirmacao.objects.values_list('emails')
    x=[]    
    for mail in emails:
        x.append(mail[0])
    if email in x:
        cod = Validacao.objects.get(email=email)
        cod1 = request.POST.get('cod1', 'None')
        cod2 = request.POST.get('cod2', 'None')
        cod3 = request.POST.get('cod3', 'None')
        cod4 = request.POST.get('cod4', 'None')
        cods = cod1 + cod2 + cod3 + cod4
        print(cods,cod.email, cod.codido)
        if cod.codido == cods:
            # usuario = authenticate(request, username=username, password=password)

            return HttpResponse('Bem vindo!')
        else:
            print(2)
            return render(request,'verificar_senha.html')
    else:
        reponse = render(request, 'login.html', {'msg': 'teste'})
        reponse.set_cookie('email',cookies['email'])
        return reponse  

