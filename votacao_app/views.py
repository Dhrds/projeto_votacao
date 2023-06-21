from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required 
from votacao_app.forms import Codigo
import random 

@login_required
def home(request):
    email = request.POST.get('email') 
    print(email)
    num = random.randint(1,9999)
    print(num)
    send_mail('assunto',num,'dhrds1996@gmail.com',[email,])
    return render(request,'login.html')

def verificar(request):
    print(1)
    user = (request.POST.get('cod1'),request.POST.get('cod2')   )
    # user += request.POST.get('cod2')   
    # user += request.POST.get('cod3')   
    # user += request.POST.get('cod4')   
    print(user)
    return render(request,'verificar_senha.html')