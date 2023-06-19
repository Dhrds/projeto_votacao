from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from allauth.socialaccount import models 

def home(request):
    if models.EmailAddress:
        user = models.EmailAddress
        print(user)
        #send_mail('assunto','corpo','dhrds1996@gmail.com',['dhrds1996@hotmail.com',])
        return HttpResponse('ola',user)
    else:
        return HttpResponse('ola mundo')