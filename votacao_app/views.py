from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail 


def home(request):
    send_mail('assunto','corpo','dhrds1996@gmail.com',['dhrds1996@hotmail.com',])
    return HttpResponse('ola')