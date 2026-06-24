from django.contrib import admin
from portal import models

@admin.register(models.Professor)  # Registrando a classe Professor no Portal do Django
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'especialidade', 'ativo',)  # ERRO 5: 'especialidade' não existe neste modelo. O campo correto é 'disciplina'

@admin.register(models.Aluno)  # Registrando a classe Aluno no Portal do Django
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Aula)  # Registrando a classe Aula no Portal do Django
class AulaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno_id', 'professor_id', 'status',)
