from django.contrib import admin
from django.urls import include, path # Adicionada a importação do include para correção da linha 6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('portal.urls')),  # Usando o include para corrigir o erro 4. Agora a URL 'cadastro/' será direcionada para as URLs definidas no arquivo portal/urls.py.
]


# Verbos HTTP - FRONTEND <-> BACKEND
#  GET -> www.escola.com -> Exiba a página home da escola.
#  POST -> www.escola.com/cadastro -> Cadastrando um novo usuário.
#  PUT -> www.escola.com/logado/alterar/1 -> Alterando o dado do usuário.
#  DELETE -> www.escola.com/logado/deletar/1 -> Deletando um usuário.
