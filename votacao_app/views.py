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
    email = request.POST.get('email')
    user = User.objects.filter(username ='atual')
    user.email = email
    print(99,user.email)
    emails = EmailConfirmacao.objects.values_list('emails')
    x=[]
    for mail in emails:
        x.append(mail[0])
    msg = x
    if user.email in x:
        num = random.randint(1000, 9999)
        num = str(num)
        cod = Validacao.objects.get(email=email)
        cod.codido = num       
        
        #send_mail('assunto',num,'votacaoproz@gmail.com',[email,])
        print(cod.codido,8)
        print(cod.codido)
        #return redirect('verificar')
        return render(request, 'verificar_senha.html')
    else:
        print('aqui',email)
        return render(request, 'login.html', {'msg': 'teste'})  


def verificar(request):
    emails = EmailConfirmacao.objects.values_list('emails')
    x=[]    
    for mail in emails:
        x.append(mail[0])
    print(request.user,88)
    user = User.objects.filter(username = 'atual')
    print(x)
    if 1 in x:
        num = random.randint(1000, 9999)
        num = str(num)
        cod = Validacao.objects.get(email=email)
        cod.codido = num       
        
        #send_mail('assunto',num,'votacaoproz@gmail.com',[email,])
        cod1 = request.POST.get('cod1', 'None')
        cod2 = request.POST.get('cod2', 'None')
        cod3 = request.POST.get('cod3', 'None')
        cod4 = request.POST.get('cod4', 'None')
        cods = cod1 + cod2 + cod3 + cod4
        print(cod.codido,8)
        print(cods, cod.codido)
        if cod.codido == cods:
            # usuario = authenticate(request, username=username, password=password)

            return HttpResponse('Bem vindo!')
        else:
            print(2)
            return render(request,'verificar_senha.html')
    else:
        print('aqui')
        return render(request, 'verificar_senha.html')   
