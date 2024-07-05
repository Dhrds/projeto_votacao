
# Página de Votação - Testes Unitários realizados usando Python

Este projeto visa demonstrar como implementar e executar testes unitários e de segurança em uma landing page desenvolvida para contabilizar votações. 

## Índice
- [Introdução](#introdução)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Configuração](#configuração)
- [Executando os Testes](#executando-os-testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Introdução do projeto
Esta é uma aplicação de votação simples onde os usuários podem votar  em uma enquete especifica determinada pelo desenvolvedor da aplicação, contudo, o foco principal deste projeto é executar testes unitários para garantir a confiabilidade, segurança e correção da aplicação.

## Funcionalidades utilizadas
- Criar e gerenciar enquetes.
- Votar em enquetes.
- Visualizar resultados das enquetes.
- Testes unitários para modelos, visualizações e outros componentes.

## Tecnologias usadas
- **Python 3.8+**
- **Django 3.2+**
- **Django REST Framework** (para endpoints da API)
- **pytest** (para o framework de testes)
- **pytest-django** (para integração do Django com pytest)

## Configuração
Para poder reproduzir o projeto é necessário que seu computador possuas os seguintes pré-requesitos:

### Pré-requisitos
- Python 3.8 ou superior
- Django 3.2 ou superior
- Editor de código-fonte compatível com as linguagens

### Etapas e Instalação
1. Clone o repositório:
2. Instale as dependências:
3. Crie um superusuário para acessar o admin do Django:
4. Execute o servidor de desenvolvimento:


## Executando os Testes
Os testes unitários são cruciais para garantir a integridade e confiabilidade da aplicação. Este projeto usa pyteste para executar os testes.

1. Certifique-se de que existe um backup do projeto;
2. Execute os testes;
3. Documente os resultados para manter um acompanhamento.

## Estrutura do Projeto
Aqui está uma breve visão geral da estrutura do projeto:

```
voting-app/
├── polls/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── voting_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Contribuindo
Contribuições são o que fazem a comunidade de código aberto ser um lugar incrível para aprender, inspirar e criar. Quaisquer contribuições que você fizer serão **muito apreciadas**.

1. Faça um fork do projeto
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/FuncionalidadeIncrivel`)
3. Commit suas mudanças (`git commit -m 'Adicionar uma FuncionalidadeIncrivel'`)
4. Push para a branch (`git push origin feature/FuncionalidadeIncrivel`)
5. Abra um Pull Request


