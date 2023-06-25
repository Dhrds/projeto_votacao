from django.db import models
from django.contrib.auth.models import User


class Validacao(models.Model):
    emails = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    codido = models.CharField(max_length=4)
    
    def __str__(self):
        return self.emails
    
class EmailConfirmacao(models.Model):
    emails = models.CharField(max_length=200)
    def __str__(self):
        return self.emails