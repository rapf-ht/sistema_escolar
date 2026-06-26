# Sistema Escolar Django

Projeto acadêmico desenvolvido em **Django** para gerenciar Professores, Alunos e Aulas. O sistema foi entregue com **8 erros intencionais** distribuídos entre models, views, forms, admin, urls e settings — e esta atividade consistiu em identificar, comentar e corrigir cada um deles.

---

## 🗂️ Estrutura do Projeto

```
sistema_escolar_django/
├── portal/               # App principal
│   ├── models.py         # Professor, Aluno, Aula
│   ├── views.py          # Views HTTP
│   ├── forms.py          # Formulários
│   ├── admin.py          # Painel admin
│   └── urls.py           # Rotas do app
├── sistema/              # Configurações do projeto
│   ├── urls.py           # Rotas globais
│   └── settings.py       # Configurações
└── manage.py
```

---

## 🐛 Erros Encontrados e Corrigidos

### Erro 01 — `portal/models.py` · Import ausente: `timezone`

**Problema:** O arquivo `models.py` utilizava `timezone.now` como valor padrão nos campos de data, mas o módulo `timezone` nunca havia sido importado. Isso causava um `NameError` imediatamente ao carregar o modelo, pois o Python não reconhecia o nome `timezone`.

**Correção:** Adicionado o import `from django.utils import timezone` no topo do arquivo.

```python
# ERRO ENCONTRADO: timezone.now é usado nos campos de data, mas o módulo não foi importado
# CORREÇÃO: adicionado 'from django.utils import timezone' no topo do arquivo
from django.utils import timezone
```

---

### Erro 02 — `portal/models.py` · Tipo de campo errado: `matricula`

**Problema:** O campo `matricula` do modelo `Aluno` foi declarado como `IntegerField`. Matrículas podem conter zeros à esquerda (ex: `"0042"`, `"00137"`), e um campo inteiro descartaria essa formatação, armazenando apenas `42` ou `137` — perdendo informação importante.

**Correção:** Alterado de `IntegerField()` para `CharField(max_length=20)`.

```python
# ERRO ENCONTRADO: matricula declarada como IntegerField, o que elimina zeros à esquerda
# CORREÇÃO: trocado para CharField para preservar a formatação completa da matrícula
matricula = models.CharField(max_length=20)
```

---

### Erro 03 — `portal/views.py` · Caminho do template errado

**Problema:** A view `index` passava o caminho do template com o prefixo `templates/`. Com `APP_DIRS: True` ativado no `settings.py`, o Django já procura automaticamente dentro da pasta `templates/` de cada app — incluir esse prefixo manualmente causava `TemplateDoesNotExist`.

**Correção:** Removido o prefixo `templates/` do caminho, deixando apenas `'portal/index.html'`.

```python
# ERRO ENCONTRADO: caminho do template inclui 'templates/' manualmente, redundante com APP_DIRS: True
# CORREÇÃO: removido o prefixo, o Django já resolve a pasta templates/ automaticamente
return render(request, 'portal/index.html')
```

---

### Erro 04 — `portal/forms.py` · Import relativo inválido

**Problema:** O formulário importava o modelo `Professor` com `from models import Professor`, um import relativo sem ponto. Em projetos Django, os módulos devem ser referenciados pelo caminho completo a partir da raiz do projeto. Esse import causava `ModuleNotFoundError` ao iniciar o servidor.

**Correção:** Substituído por `from portal.models import Professor`.

```python
# ERRO ENCONTRADO: import relativo 'from models import Professor' é inválido no Django
# CORREÇÃO: trocado pelo caminho absoluto 'from portal.models import Professor'
from portal.models import Professor
```

---

### Erro 05 — `portal/admin.py` · Campo inexistente no `list_display`

**Problema:** O `list_display` da classe `ProfessorAdmin` referenciava o campo `'especialidade'`, que pertencia ao sistema médico usado como base para este projeto. No sistema escolar, o campo equivalente é `'disciplina'`. O Django lançava um erro ao tentar exibir uma coluna que não existe no modelo.

**Correção:** Substituído `'especialidade'` por `'disciplina'` no `list_display`.

```python
# ERRO ENCONTRADO: 'especialidade' não existe no modelo Professor do sistema escolar
# CORREÇÃO: substituído por 'disciplina', que é o campo correto neste contexto
list_display = ('id', 'nome', 'email', 'telefone', 'disciplina', 'ativo',)
```

---

### Erro 06 — `portal/urls.py` · View inexistente referenciada

**Problema:** O arquivo de URLs do app registrava a rota `'cadastro/'` apontando para `views.cadastro`, mas essa função não existia em `views.py`. O Django lançava `AttributeError` ao importar o módulo de URLs.

**Correção:** Removida a rota `'cadastro/'` das `urlpatterns`, pois a view correspondente ainda não foi implementada.

```python
# ERRO ENCONTRADO: views.cadastro referenciada na URL, mas essa função não existe em views.py
# CORREÇÃO: linha removida das urlpatterns; a rota só deve ser registrada quando a view existir
urlpatterns = [
    path('index/', views.index),
]
```

---

### Erro 07 — `sistema/urls.py` · Sintaxe inválida no `urlpatterns`

**Problema:** O arquivo de URLs principal continha texto livre dentro do `urlpatterns` (`preciso mostrar a página cadastro.html`), que não é código Python válido. Isso causava um `SyntaxError` imediato ao iniciar o servidor, impedindo que qualquer outra parte do projeto fosse carregada.

**Correção:** Linha inválida removida. Este foi o primeiro erro corrigido, pois bloqueava completamente a inicialização do servidor.

```python
# ERRO ENCONTRADO: texto livre dentro de urlpatterns causava SyntaxError ao iniciar o servidor
# CORREÇÃO: linha inválida removida; include() deve ser usado para incluir URLs de outros apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
]
```

---

### Erro 08 — `sistema/settings.py` · App `portal` não registrado no `INSTALLED_APPS`

**Problema:** O app `'portal'` havia sido removido da lista `INSTALLED_APPS`. Sem esse registro, o Django ignora completamente o app — os models não aparecem nas migrations, os templates não são encontrados e o admin não exibe nenhuma das classes cadastradas.

**Correção:** Adicionado `'portal'` à lista `INSTALLED_APPS`.

```python
# ERRO ENCONTRADO: o app 'portal' não estava em INSTALLED_APPS, sendo completamente ignorado pelo Django
# CORREÇÃO: adicionado 'portal' à lista para que models, templates e admin funcionem corretamente
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal',
]
```

---

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos

- Python 3.10+
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/sistema_escolar_django.git
cd sistema_escolar_django

# 2. Crie e ative o ambiente virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 3. Instale as dependências
pip install django

# 4. Aplique as migrations
python manage.py makemigrations
python manage.py migrate

# 5. Crie um superusuário (para acessar o admin)
python manage.py createsuperuser

# 6. Inicie o servidor
python manage.py runserver
```
---

## 👨‍💻 Autor

**Rafael Ferreira**  
Estudante de Análise e Desenvolvimento de Sistemas
GitHub: [github.com/rapf-ht](https://github.com/rapf-ht)  
LinkedIn: [linkedin.com/in/rafael-ferreira-ht](https://linkedin.com/in/rafael-ferreira-ht)