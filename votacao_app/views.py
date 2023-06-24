from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from votacao_app.forms import Codigo
from django.template import Template
import random
cod = 'a'

# @login_required


def home(request):
    email = request.POST.get('email')
    msg = ''
    print(email)
    if email in ['asd@asd.com', 'asdf@asdf.com']:
        print(123)
        num = random.randint(1000, 9999)
        num = str(num)
        global cod
        cod = num
        print(cod)
        # send_mail('assunto',num,'dhrds1996@gmail.com',[email,])
        email = None
        return redirect(verificar)
    elif email == None:
        email = None
        return render(request, 'login.html', {'msg': msg})
    else:
        email = None
        msg = 'Email invalido'
        return render(request, 'login.html', {'msg': msg})


def verificar(request):
    print(1)
    cod1 = request.POST.get('cod1', 'None')
    cod2 = request.POST.get('cod2', 'None')
    cod3 = request.POST.get('cod3', 'None')
    cod4 = request.POST.get('cod4', 'None')
    cods = cod1 + cod2 + cod3 + cod4
    print(cods, cod)
    if cod == cods:
        # usuario = authenticate(request, username=username, password=password)

        return HttpResponse('Bem vindo!')
    else:
        print(2)
        return render(request, 'verificar_senha.html')
