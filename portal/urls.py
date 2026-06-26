from django.urls import path

from portal import views

# exemplo: path('index/', views.index)
urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro),  # View cadastro criada no portal/views.py
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
