from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required 
from votacao_app.models import Email

@login_required
def home(request):
    user = Email.codigo('cod1')    
    print(user)
    #send_mail('assunto','corpo','dhrds1996@gmail.com',['dhrds1996@hotmail.com',])
    return render(request,'login.html')

def verificar(request):
    print(1)
    user = Email.codigo('cod1')    
    print(user,8)
    return render(request,'verificar_senha.html')