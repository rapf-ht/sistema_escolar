from django.shortcuts import render

# GET, POST, PUT, DELETE
# REQUEST <-> RESPONSE
# RENDER -> RENDERIZAR

# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA INDEX - USE FUNÇÃO
def index(request):  # É a request feita pelo usuário
    return render(
        request,
        'portal/index.html'  # Endereço do template corrigido
    )

# Criando a view para cadastro:

def cadastro(request):
    return render(
        request,
        'portal/cadastro.html'
    )