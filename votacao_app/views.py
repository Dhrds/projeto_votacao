from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required 
from votacao_app.forms import Codigo

@login_required
def home(request):
    user = request.POST.get('email') 
    print(user)
    #send_mail('assunto','corpo','dhrds1996@gmail.com',['dhrds1996@hotmail.com',])
    return render(request,'login.html')

def verificar(request):
    print(1)
    user = request.POST.get('cod1')   
    print(user)
    return render(request,'verificar_senha.html')