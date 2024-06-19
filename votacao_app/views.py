from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Aluno, Grupo, Votacao
from django.contrib.auth import  login
from django.http import Http404
import random 
from .uteis import send_html_mail

def html(email1):
    aluno = Aluno.objects.get(email=email1)
    num = random.randint(1000, 9999)
    num = str(num)
    aluno.codigo = num
    aluno.save()
    return f'''
            <html>
                <body>
                    <div style="box-sizing:border-box;width:600px;display:block;background-color:#fff;font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;padding:40px;border-radius:2px;border:solid 1px #efefef;text-align:center;margin-top:1rem"
    id="m_-8812820040621664389__body__">
    <div style="font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0 0 30px 0">Oi,
        {aluno.nome}</div>
    <div style="font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0 0 30px 0">
        <h1
            style="text-align:center;font-size:20px;color:#323232;font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0;line-height:24px">
            Seu código para autenticação</h1>
    </div>
    <div style="font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0 0 30px 0">
        <p
            style="text-align:center;margin:0;padding:0;color:#323232;line-height:22px;font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif">
            Recebemos uma solicitação de acesso à sua conta. Utilize o código abaixo para confirmar:</p>
    </div>
    <div style="font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0 0 30px 0">
        <center>
            <div
                style="background:#f9f9f9;padding-top:9px;padding-bottom:7px;padding-left:39px;padding-right:36px;width:163px;height:41px">
                <p
                    style="text-align:center;margin:0;padding:0;color:#323232;line-height:25px;font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;font-size:18px;font-weight:bold;letter-spacing:4.5px;padding-top:9px">
                    {num}</p>
            </div>
        </center>
    </div>
    <div style="font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0 0 30px 0">
        <p
            style="text-align:center;margin:0;padding:0;color:#999999;line-height:16px;font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;font-size:12px">
            Código válido para acesso.</p>
    </div>
    <div style="font-family:Verdana,'Helvetica Neue',HelveticaNeue,Helvetica,Arial,sans-serif;margin:0 0 30px 0">
        <hr style="border:0;height:1px;background-color:#e1e1e1;width:429px">
    </div>

</div>
                </body>
            </html>
            '''


def home(request):
    msg = request.session.get('messages', None)
    return render(request, 'login.html', {'messages': msg})


def check(request):
    if not request.POST:
        raise Http404
    email = request.POST.get('email')
    try:
        send_html_mail('teste',html(email),['dhrds1996@gmail.com'],['noreply@thehobbymania.com'])        
        request.session['email'] = email
        return redirect('verificar')
    except Aluno.DoesNotExist:
        request.session['messages'] = 'email-nao-cadastrado'
        return redirect('home')

def verificar(request):
    email = request.session.get('email', None)
    if Aluno.objects.values_list('email').exists():
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
                user.save
                login(request, user)
                print(user.is_authenticated)
                return redirect('votacao')
            except:
                user = User.objects.create_user(
                    cod.nome, cod.email, cod.codigo)
                login(request, user)
            return redirect(votacao)
        else:
            return render(request, 'verificar_senha.html')
    else:
        reponse = render(request, 'login.html', {'msg': 'teste'})
        return reponse


def votacao(request):

    user = request.user
    if user.is_authenticated:
        grupos = Grupo.objects.values_list('nome_grupo')
        if user.username:
            aluno = Aluno.objects.get(nome=user.username)
        grupos_tratados = []
        for i in grupos:
            grupos_tratados.append(i[0])
        voto = request.POST.get('grupo')
        grupos_tratados.remove(aluno.grupo.nome_grupo)
        print(voto, Votacao.objects.filter(aluno=user.username).exists())
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
        return redirect('home')


