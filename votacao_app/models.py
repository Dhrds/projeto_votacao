from django.db import models
from django.contrib.auth.models import User


class Validacao(models.Model):
    email = models.CharField(max_length=200,unique=True)
    codido = models.CharField(max_length=4)
    
    def __str__(self):
        return self.email
    
class EmailConfirmacao(models.Model):
    emails = models.CharField(max_length=200)
    def __str__(self):
        return self.emails