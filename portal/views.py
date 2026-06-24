from django.shortcuts import render

# GET, POST, PUT, DELETE
# REQUEST <-> RESPONSE
# RENDER -> RENDERIZAR

# CRIANDO UMA VIEW PARA APRESENTAR A PÁGINA INDEX - USE FUNÇÃO
def index(request):  # É a request feita pelo usuário
    return render(
        request,
        'templates/portal/index.html'  # ERRO 2: caminho errado. Deve ser 'portal/index.html'
    )
