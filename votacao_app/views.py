from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

@login_required
def home(request):
    user = User.is_authenticated
    print(user)
    #send_mail('assunto','corpo','dhrds1996@gmail.com',['dhrds1996@hotmail.com',])
    return render(request,'login.html')

def verificacao(request):
    return render(request,'verificar_senha.html')