from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('verificar/',views.verificacao,name='verificar_senha'),

    
]