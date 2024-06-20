from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Aluno, Grupo, Votacao

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.grupo = Grupo.objects.create(nome_grupo='GrupoTest')
        self.aluno = Aluno.objects.create(nome='TestUser', email='test@example.com', codigo='1234', grupo=self.grupo)
        self.user = User.objects.create_user(username='TestUser', email='test@example.com', password='1234')
        self.aluno.grupo = self.grupo
        self.aluno.save()
        self.votacao = Votacao.objects.create(aluno='TestUser', grupo='GrupoTest')
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_check_view_post_valid_email(self):
        response = self.client.post(reverse('check'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('verificar'))
        self.assertIn('email', self.client.session)
    
    def test_check_view_post_invalid_email(self):
        response = self.client.post(reverse('check'), {'email': 'invalid@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(self.client.session['messages'], 'email-nao-cadastrado')
    
    def test_verificar_view_get(self):
        session = self.client.session
        session['email'] = 'test@example.com'
        session.save()
        response = self.client.get(reverse('verificar'))
        self.assertEqual(response.status_code, 200)
    
    def test_verificar_view_post_correct_code(self):
        session = self.client.session
        session['email'] = 'test@example.com'
        session.save()
        response = self.client.post(reverse('verificar'), {'cod1': '1'})
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('votacao'))
    
    def test_verificar_view_post_incorrect_code(self):
        session = self.client.session
        session['email'] = 'test@example.com'
        session.save()
        response = self.client.post(reverse('verificar'), {'cod1': '0', 'cod2': '0', 'cod3': '0', 'cod4': '0'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'verificar_senha.html')
    
    def test_votacao_view_authenticated(self):
        self.client.login(username='TestUser', password='1234')
        response = self.client.get(reverse('votacao'))
        self.assertEqual(response.status_code, 200)
    
    def test_votacao_view_vote(self):
        self.client.login(username='TestUser', password='1234')
        response = self.client.post(reverse('votacao'), {'grupo': 'GrupoTest'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmar-voto.html')
    
    def test_votacao_view_unauthenticated(self):
        response = self.client.get(reverse('votacao'))
        self.assertRedirects(response, reverse('home'))

